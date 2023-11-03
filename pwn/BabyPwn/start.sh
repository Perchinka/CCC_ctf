#!/bin/sh
gcc -o babypwn main.c -z norelro -fno-stack-protector;
rm main.c


# DO NOT DELETE
/etc/init.d/xinetd start;
sleep infinity;
