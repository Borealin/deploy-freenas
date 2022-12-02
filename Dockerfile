FROM python:latest
RUN pip install requests schedule
COPY . /app
WORKDIR /app
VOLUME /app/config /app/acme
CMD ["python", "-u", "run.py"]