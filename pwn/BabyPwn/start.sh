#!/bin/sh
gcc -o vuln main.c -z norelro -fno-stack-protector;
rm main.c

socat tcp-l:9999,reuseaddr,fork EXEC:"/home/ctf/vuln"
