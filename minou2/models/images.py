from itertools import islice
from ..providers import shutterstock, local
from .. import celery_app

providers = [
        {'module': shutterstock, 'weight': 0.9},
        {'module': local, 'weight': 1.0}
]

@celery_app.task
def search(concept):
    weight = float(concept['relevance'])
    images = []
    for provider in providers:
        images.append([(provider['weight'] * weight, i)
            for i in provider['module'].fetch(concept)])

    # weight by positions
    images = [(w * (1-n/len(l)), i) for l in images for n,(w,i) in enumerate(l)]

    # sort by weight
    images = reversed(sorted(images, key=lambda i:i[0]))

    # keep top 10 images
    return list(islice(images, 10))

