# FROM python:3.7
FROM python:3.8-slim

RUN mkdir /code
WORKDIR /code
# RUN apt-get update 
# RUN apt-get install ffmpeg libsm6 libxext6  -y 
RUN apt-get update && apt-get install --no-install-recommends supervisor openssh-server rsyslog nano curl ffmpeg libsm6 libxext6 -y && \
    rm -rf /var/lib/apt/lists/*
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt --no-cache-dir

COPY ./app /code/app

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf


RUN mkdir /var/run/sshd
RUN echo 'root:mypassword' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN sed -i '/imklog/s/^/#/' /etc/rsyslog.conf

EXPOSE 22


# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

CMD ["/usr/bin/supervisord"]