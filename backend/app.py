
import uuid
from flask import Flask, g, jsonify, request, json
from flask_oidc import OpenIDConnect
from flask_cors import CORS, cross_origin
# from entities.request import Request
from dataaccess.requestsDataAccess import RequestDataAccess
from utils.jsonClassEncoder import JsonClassEncoder
from config import init_app
from utils.util import cors_preflight
import os
from datetime import datetime, timedelta
import glob

# configuration
DEBUG = True

app = init_app()

requestDataAccess = RequestDataAccess()
jsonClassEncoder = JsonClassEncoder()

oidc = OpenIDConnect(app)

@app.route('/')
def home():
    if oidc.user_loggedin:
        return("Hello,%s"%oidc.user_getfield('email'))
    else:
        return 'Welcome, please <a href="/dashboard">Login</a>'

@app.route('/dashboard')
@oidc.require_login
@cross_origin()
def dashboard():
    userinfo = oidc.user_getinfo(['email','preferred_username','sub'])

    username = userinfo.get('preferred_username')
    email  = userinfo.get('email')
    userid = userinfo.get('sub')

    return("This is your dashboard, %s and your email is %s! and UserId is %s"%(username,email,userid))

@app.route('/user')
@oidc.accept_token(True)
def user():
    email = g.oidc_id_token['email']
    userid = g.oidc_id_token['sub']
    username = g.oidc_id_token['preferred_username']
    userobject = {'Name':username,'Email':email,'ID':userid}
    response = jsonify(userobject)
    return response

# sanity check route
@app.route('/ping', methods=['GET'])
@cors_preflight('GET,POST,OPTIONS')
@oidc.accept_token(True)
def ping_pong():
    return jsonify('pong!')

@app.route('/requests/upload/<requestid>', methods=['GET','POST'])
@cors_preflight('GET,POST,OPTIONS')
@oidc.accept_token(True)
def file_upload(requestid):  
    fileStorage = request.files['image']
    uploadFolder = app.config['UPLOAD_FOLDER'] + requestid + '/' 
    if not os.path.isdir(uploadFolder):
        os.mkdir(uploadFolder)
    fileName = fileStorage.filename.split(".")
    fileStorage.save(os.path.join(uploadFolder, fileName[0] + datetime.now().strftime("%m%d%Y%H%M%S") + '.' + fileName[1]))
    list_of_files = glob.glob(uploadFolder+'*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file = latest_file.replace("\\", "/")
    print(latest_file)
    print(' * received form with', request.files['image'])  
    return jsonClassEncoder.encode(True), 200

@app.route('/requests/<requestid>', methods=['PUT', 'DELETE'])
@cors_preflight('GET,POST,PUT,DELETE,OPTIONS')
@oidc.accept_token(True)
def single_request(requestid):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        requestjson = request.get_json()
        name = requestjson['name']
        description = requestjson['description']
        status = requestjson['status']
        createdby = requestjson['createdby']   
        updated = requestjson['updated']
        requestaddresult = requestDataAccess.EditRequest(requestid, name, description, status, createdby, updated)
        response_object['message'] = 'Request updated!'
    if request.method == 'DELETE':
        requestaddresult = requestDataAccess.DeleteRequest(requestid)
        response_object['message'] = 'Request removed!'
    if requestaddresult.success == True:
        return jsonClassEncoder.encode(requestaddresult), 200
    else:
        return jsonClassEncoder.encode(requestaddresult), 500

@app.route('/requests/add', methods = ['POST', 'GET'])
@cors_preflight('GET,POST,OPTIONS')
@oidc.accept_token(True)
def addrequest():
    requestjson = request.get_json()

    name = requestjson['name']
    description = requestjson['description']
    status = requestjson['status']
    createdby = requestjson['createdby']   
    updated = requestjson['updated']

    requestaddresult = requestDataAccess.AddRequest(name, description, status, createdby, updated)
    if requestaddresult.success == True:
        return jsonClassEncoder.encode(requestaddresult), 200
    else:
        return jsonClassEncoder.encode(requestaddresult), 500

@app.route('/requests/all')
@cors_preflight('GET,POST,OPTIONS')
@oidc.accept_token(True)
def getallrequests():
    requests = requestDataAccess.GetRequests()
    jsondata = json.dumps(requests)
    return jsondata, 200


if __name__ == '__main__':
    app.run(debug=True)