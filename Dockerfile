# Dcokerfile
FROM python:3.9

# wait hosts app
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

# work directory
WORKDIR /home/kitya
RUN mkdir -p /home/kitya/app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm requirements.txt

# copy main code
COPY app app
COPY main.py main.py
COPY config.py config.py
COPY wsgi.py wsgi.py

# run flask app with gunicorn
EXPOSE 5000
CMD ["python3", "-m", "gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "wsgi:app"]
