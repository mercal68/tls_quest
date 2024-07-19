FROM python:3.8-slim

ADD my_app.py /home/my_app.py
WORKDIR /home/
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["/home/my_app.py"]
ENTRYPOINT ["python"]
