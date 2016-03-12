from . import auth
from . import anal

def Api(app):
    # # POST /auth
    # Authenticate a user.
    #
    # Request must include a  |username| and |password| field that will be used
    # to find and validate the user.
    #
    # The response contains the "token" field to be used in following
    # authenticated requests set in the "X-Auth-Token" header.
    app.add_url_rule('/auth', 'auth', auth.auth, methods=['POST'])

    # POST /anal
    # Create a new analysis job for a given text.
    #
    # The request should contains the |data| field containing the text to be
    # analyzed. The response should contains the |job| field that can later be
    # reused to poll the task status and get the task result.
    app.add_url_rule('/anal', 'anal', anal.create, methods=['POST'])

