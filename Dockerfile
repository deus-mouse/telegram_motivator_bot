FROM python:3.7

RUN mkdir -p /usr/src/motivator-bot/
RUN apt update

WORKDIR /usr/src/motivator-bot/

COPY . /usr/src/motivator-bot/
RUN pip install --no-cache-dir -r req.txt

CMD ["python", "run.py"]