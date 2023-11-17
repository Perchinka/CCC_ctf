#!/bin/sh

socat tcp-l:9999,reuseaddr,fork EXEC:"/home/ctf/main.py",pty,stderr
