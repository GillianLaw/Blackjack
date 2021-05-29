ans = int('{:032b}'.format(10000000001000000000101000000001))
print(ans)


# ans1 = int(format(10000000001000000000101000000001, '032b')
# print(ans1)

ip = '128.32.10.1'
addr = ip.split(".")
res = int(addr[0]) << 24
res += int(addr[1]) << 16
res += int(addr[2]) << 8
res += int(addr[3])
print(addr)
print(res)