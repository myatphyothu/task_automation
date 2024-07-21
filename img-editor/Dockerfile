FROM python:3.11.9

COPY *.py .
COPY requirements.txt .
COPY settings.json .
COPY docker.properties .

RUN pip install -r requirements.txt
CMD python run_with_user_inputs.py