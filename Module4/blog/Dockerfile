# Build a clean virtualenv and install system libraries
FROM python:3.11-slim AS build
RUN apt update && \
    apt install python3-dev -y && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip

# Build the virtualenv when requirements.txt changes
FROM build AS build-venv
ENV PATH="/venv/bin:$PATH"
COPY ./webhook/requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt


# Copy the app, the virtualenv and system libraries
FROM python:3.11-slim as run
ENV PATH="/venv/bin:$PATH"
COPY --from=build /usr/lib/ /usr/lib/
COPY --from=build-venv /venv /venv

RUN useradd -ms /bin/bash webapp -u 1234 -d /home/webapp

COPY ./webhook/ /home/webapp/webhook/
RUN chown -R webapp:webapp /home/webapp/

USER 1234
EXPOSE 5000
WORKDIR /home/webapp/
CMD /venv/bin/gunicorn --workers 4 \
  --threads 50 \
  --bind 0.0.0.0:5000 \
  --reload \
  --log-level $LOG_LEVEL \
  --timeout $GUNICORN_TIMEOUT \
  --certfile=$TLS_CERT \
  --keyfile=$TLS_KEY \
  webhook:admission_controller
