import requests
import json


URL = 'https://remoteok.io/api'
keys = ['date', 'company', 'location', 'position', 'tags', 'url']

def get_jobs(*wanted_tags):
    resp = requests.get(URL)
    job_results = resp.json()

    jobs = []
    for i,listing in enumerate(job_results):
        job = {k: v for k,v in listing.items() if k in keys}
        #print(f'{i+1}. {filtered}')
        if job:
            tags = {tag.lower() for tag in job.get('tags')}
            if tags.intersection(wanted_tags):
                jobs.append(job)

    return jobs




