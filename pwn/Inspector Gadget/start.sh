#!/bin/sh
gcc -g -o vuln main.c -no-pie -fno-stack-protector
rm main.c

socat tcp-listen:9999,reuseaddr,fork EXEC:"/home/ctf/vuln"
