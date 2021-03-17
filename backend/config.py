from flask import Flask
from flask_cors import CORS, cross_origin
from flask_oidc import OpenIDConnect
from utils.db import db

def init_app():
    app = Flask(__name__)
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
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI':'postgresql://postgres:password@localhost:5432/reviewdb',
        'UPLOAD_FOLDER': 'c://AOT/Files/'
      
    })

    db.init_app(app)    
    return app
    