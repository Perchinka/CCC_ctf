from pwn import *

p = remote('alex.lukin.family', 1345)

while True:
    exp = p.recvline()
    print(exp)
    p.sendline(str(eval(exp)).encode())
   
