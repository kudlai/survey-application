FROM alpine


COPY webapp /webapp

RUN apk --update add py-pip gcc libc-dev linux-headers pcre-dev python-dev &&\
    pip install uwsgi &&\
    pip install -r /webapp/requirements.txt &&\
    apk del  python-dev linux-headers libc-dev gcc && \
    rm -rf /var/cache/apk/* && \
    adduser -D -u 1001 noroot



ENV HOME /webapp
WORKDIR /webapp
 
# Expose port 8000 for uwsgi
EXPOSE 8000
 
ENTRYPOINT ["uwsgi", "--plugin", "http,python", "--http", "0.0.0.0:8000", "--module", "app:app", "--processes", "1", "--threads", "8"]
