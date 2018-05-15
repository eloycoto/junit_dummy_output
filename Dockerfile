FROM python:3

WORKDIR /opt/dummy/

RUN pip install nose

VOLUME /opt/dummy/

ENTRYPOINT /usr/local/bin/nosetests --with-xunit
