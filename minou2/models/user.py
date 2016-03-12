fixtures = {
        'bob': {'password': '1234', 'id': 1}
}
def auth(username, password):
    if username in fixtures and fixtures[username]['password'] == password:
        return str(fixtures[username]['id'])
    return None

