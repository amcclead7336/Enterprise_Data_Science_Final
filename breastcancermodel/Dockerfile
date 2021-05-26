FROM python:3.7.0
MAINTAINER Cesar Martinez, Northwestern University
COPY ./flask_apps /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python breast_cancer_flask.py