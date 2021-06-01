FROM python:3.8-alpine
ENV PYBASE=/pybase \
    PYTHONUSERBASE=$PYBASE \
    PATH=$PYBASE/bin:$PATH 

RUN pip install pipenv

WORKDIR /tmp
COPY Pipfile .
RUN pipenv lock && \
    PIP_USER=1 \
    PIP_IGNORE_INSTALLED=1 \
    pipenv install -d --system --ignore-pipfile

COPY . /app/worker/
WORKDIR /app/worker/

CMD ["python", "worker.py"]