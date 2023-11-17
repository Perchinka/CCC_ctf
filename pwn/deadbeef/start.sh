#!/bin/sh
gcc -m32 -o vuln main.c -no-pie -fno-stack-protector
rm main.c

socat tcp-l:9999,reuseaddr,fork EXEC:"/home/ctf/vuln",pty,stderr
