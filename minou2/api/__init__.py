def Api(app):
    @app.route('/ping')
    def ping():
        return 'echo'
