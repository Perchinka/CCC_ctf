#!/bin/sh
socat tcp-listen:9999,reuseaddr,fork EXEC:"/home/ctf/vuln"
