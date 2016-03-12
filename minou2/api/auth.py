import itsdangerous
from flask import current_app, request, abort, jsonify
from ..models import user

# Authenticate a user, given a username and password. The response contains
# the "token" field to be used in following authenticated requests set in
# the "X-Auth-Token" header.
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    user_id = user.auth(username, password)
    if not user_id:
        abort(401)
    current_app.logger.info('Authenticating user "{}"'.format(user_id))

    s = itsdangerous.Signer(current_app.config['AUTH_SECRET'])
    return jsonify(**{
        'token': s.sign(user_id.encode()).decode('utf-8')
    })
