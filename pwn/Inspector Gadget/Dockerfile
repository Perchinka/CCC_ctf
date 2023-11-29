FROM ubuntu:16.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y socat gcc

RUN useradd -m ctf

WORKDIR /home/ctf

COPY ./start.sh /start.sh

COPY ./src/ /home/ctf/
RUN chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag.txt && \
    chmod ugo+rx /start.sh && chmod ugo-w /start.sh

RUN gcc -g -o vuln main.c -no-pie -fno-stack-protector && \
    rm main.c

CMD ["/start.sh"]

EXPOSE 9999
