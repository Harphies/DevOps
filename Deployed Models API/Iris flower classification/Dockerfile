FROM python:3.6.5
COPY . /usr/local/python/
EXPOSE 3000
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python app.py