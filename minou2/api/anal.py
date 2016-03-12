from flask import current_app, request, abort, jsonify
from .. import analysis

def create():
    '''Create a new text analysis job'''
    text = request.form.get('text')
    job = analysis.analyze.delay(text)
    return jsonify(**{'job': job.id}), 202 # ACCEPTED


