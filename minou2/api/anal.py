from flask import current_app, request, abort, jsonify
from .. import analysis

def create():
    '''Create a new text analysis job'''
    text = request.form.get('text')
    job = analysis.analyze.delay(text)
    return jsonify(**{'job': job.task_id}), 202 # ACCEPTED

def poll(task_id):
    task = analysis.analyze.AsyncResult(task_id)
    if task.successful():
        return jsonify(**{'status': task.status, 'result': task.result})
    return jsonify(**{'status': task.status})

