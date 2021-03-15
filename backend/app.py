
import uuid
from flask import Flask, g, jsonify, request, json
from flask_oidc import OpenIDConnect
from flask_cors import CORS, cross_origin

# configuration
DEBUG = True

app = Flask(__name__)

# enable CORS
CORS(app)

app.config.update({
    'SECRET_KEY': 'foiclientapp',
    'TESTING': True,
    'DEBUG': True,    
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_VALID_ISSUERS': ['https://iam.aot-technologies.com/auth/realms/foirealm'],
    'OIDC_OPENID_REALM': 'http://localhost:5000/oidc_callback',  
})

oidc = OpenIDConnect(app)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


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
    email = g.oidc_token_info['email']
    userid = g.oidc_token_info['sub']
    username = g.oidc_token_info['username']
    userobject = {'Name':username,'Email':email,'ID':userid}

    return("This is your dashboard, %s and your email is %s! and UserId is %s"%(jsonify(userobject)))

@app.route('/user')
@oidc.accept_token(True)
def user():
    
    email = g.oidc_token_info['email']
    userid = g.oidc_token_info['sub']
    username = g.oidc_token_info['username']
    userobject = {'Name':username,'Email':email,'ID':userid}
    response = jsonify(userobject)

    return response    

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)



@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)