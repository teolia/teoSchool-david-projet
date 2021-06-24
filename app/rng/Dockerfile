FROM python:3.8-alpine as builder
ENV PYBASE=/pybase 
ENV PYTHONUSERBASE=$PYBASE 
ENV PATH=$PYBASE/bin:$PATH 

RUN pip install pipenv

WORKDIR /tmp
COPY Pipfile .
RUN pipenv lock && \
    PIP_USER=1 \
    PIP_IGNORE_INSTALLED=1 \
    PIPENV_VENV_IN_PROJECT=1 \
    pipenv install -d

# final
FROM python:3.8-alpine

COPY --from=builder /tmp/.venv /venv
ENV PATH="/venv/bin:$PATH"
ENV FLASK_APP="rng"

RUN addgroup --system app \
    && adduser -S -G app app

WORKDIR /home/app

USER app

COPY . .

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "rng:app"]
