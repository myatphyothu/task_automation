import my_mailer
import json
import job_tracker

#mail.send('this is a test message')


jobs = job_tracker.get_jobs('python')
if len(jobs) > 0:

    #message = "Subject: Python Remote Jobs!\n\n"

    msg = "<html><body>"
    msg += "There are some remote python jobs<br/>"

    msg += "<table>"
    
    msg += '<th>'
    for k in job_tracker.keys:
        msg += f'<td><b>{k}</b></td>'
    msg += '<th>'

    for job in jobs:
        #msg += f"{json.dumps(job)}\n\n"
        
        msg += "<tr>"
        for k in job_tracker.keys:
            #msg += f'<td><b>{k}</b></td>'
            
            msg += f"<td>{job[k]}</td>"
        msg += "</tr>"

    msg += "</table>"
    msg += "</body></html>"
    
    my_mailer.send(sender='phyothu.myat@gmail.com', receiver='phyothu.myat@gmail.com', subject='Python Remote Jobs!', content=msg)
