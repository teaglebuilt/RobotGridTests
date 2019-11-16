FROM python:3.6

ADD . /cao_ui_tests

WORKDIR /cao_ui_tests

RUN pip install -r requirements.txt

RUN chmod +x scripts/wait_for_it.sh