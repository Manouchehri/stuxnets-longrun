from .auth import auth

def Api(app):
    app.add_url_rule('/auth', 'auth', auth, methods=['POST'])

