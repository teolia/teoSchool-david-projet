FROM python:3.8-alpine
ENV PYBASE=/pybase 
ENV PYTHONUSERBASE=$PYBASE 
ENV PATH=$PYBASE/bin:$PATH 
ENV FLASK_APP="rng"

RUN pip install pipenv

WORKDIR /tmp
COPY Pipfile .
RUN pipenv lock && \
    PIP_USER=1 \
    PIP_IGNORE_INSTALLED=1 \
    pipenv install -d --system --ignore-pipfile

COPY . /app/rng/
WORKDIR /app/rng/
EXPOSE 80
CMD ["flask", "run", "--port=80", "--host=0.0.0.0"]