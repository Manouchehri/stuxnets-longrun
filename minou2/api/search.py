from itertools import islice
from celery import group
from celery.result import GroupResult
from flask import current_app, request, abort, jsonify
from ..models import images
from .. import analysis, celery_app

def create():
    analysis_task_id = request.form.get('analysis')
    analysis_job = analysis.analyze.AsyncResult(analysis_task_id)
    if not analysis_job.successful():
        abort(500)

    analysis_result = analysis_job.get()
    searches = group([images.search.s(keyword) for keyword in analysis_result['keywords']])
    job = searches.apply_async()
    job.save()
    return jsonify(**{'job': job.id})

def poll(task_id):
    task = celery_app.GroupResult.restore(task_id)
    if task.successful():
        results = task.results
        # flatten results
        results = [x for l in results for x in l.result]

        # sort by weight
        results = list(islice(reversed(sorted(results, key=lambda x:x[0])), 10))

        # keep the top 10 images
        return jsonify(**{'status': 'SUCCESS', 'result': [image for _, image in results]})
    return jsonify(**{'status': 'PENDING'})

