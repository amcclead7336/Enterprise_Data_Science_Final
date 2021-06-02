FROM python:3.7.8
MAINTAINER Alex McClead, Northwestern Student
COPY ./api /usr/local/python/api
COPY ./LogisticRegression-model /usr/local/python/LogisticRegression-model
EXPOSE 5010
WORKDIR /usr/local/python/api/
RUN pip install -r requirements.txt
CMD python FlaskAPI.py