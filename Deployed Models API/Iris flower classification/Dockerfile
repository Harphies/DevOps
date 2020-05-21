FROM continuum/anaconda:4.4.0
CPOY . /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python app.py