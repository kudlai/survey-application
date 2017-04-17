FROM alpine


COPY webapp /webapp

RUN apk --update add gettext py-pip python-dev py-mysqldb py-yaml uwsgi uwsgi-http uwsgi-python uwsgi-corerouter &&\
    pip install -r /webapp/requirements.txt &&\
    rm -rf /var/cache/apk/* && \
    adduser -D -u 1001 noroot

ENV HOME /webapp
WORKDIR /webapp
 
# Expose port 8000 for uwsgi
EXPOSE 8000
 
CMD     envsubst < /webapp/config.yaml.tpl > /webapp/config.yaml; uwsgi --plugin http,python --http 0.0.0.0:8000 --module app:app --processes 1 --threads  8 --uid noroot --gid noroot
