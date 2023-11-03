#!/bin/sh
gcc -m32 -o deadbeef main.c -no-pie -fno-stack-protector
rm main.c


# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
