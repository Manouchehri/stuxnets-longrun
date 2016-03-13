from flask import current_app, request, abort, jsonify
from .. import analysis

def find(analysis_task_it):
    analysis_job = analysis.analyze.AsyncResult(task_id)
    if not analysis_job.successful():
        abort(500)

    analysis = analysis_job.get()
    find.group(analysis)
