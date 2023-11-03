#!/bin/sh
gcc -m32 -o return_time main.c -no-pie -fno-stack-protector
rm main.c


# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
