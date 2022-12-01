FROM python:latest
RUN pip install requests schedule
COPY . /app
WORKDIR /app
VOLUME /app/config
CMD ["python", "run.py"]