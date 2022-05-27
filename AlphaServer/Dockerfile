FROM python:3.8-slim

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install --no-install-recommends supervisor openssh-server rsyslog nano curl ffmpeg libsm6 libxext6 -y && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd
RUN echo 'root:mypassword' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN sed -i '/imklog/s/^/#/' /etc/rsyslog.conf


COPY ./AlphaServer/start.sh /code/start.sh
RUN chmod +x /code/start.sh

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]