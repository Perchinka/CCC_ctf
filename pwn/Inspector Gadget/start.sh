#!/bin/sh
socat tcp-listen:9999,reuseaddr,fork EXEC:"setarch -R /home/ctf/vuln"
