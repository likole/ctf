# from flag import flag
# assert flag.startswith("flag{")
# assert flag.endswith("}")
# assert len(flag)==27

def nlfsr(R,mask):
    output = (R << 1) & 0xffffff
    i=(R&mask)&0xffffff
    lastbit=0
    changesign=True
    while i!=0:
        if changesign:
            lastbit &= (i & 1)
            changesign=False
        else:
            lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)

mask=0b110110011011001101110

ans=[]
f=open("key","rb")
s=f.read(1024*1024)
for i in s:
    ans.append(i)
print(len(ans))

def test(R):
    c=R
    for i in range(1024 * 1024):
        tmp = 0
        for j in range(8):
            (R, out) = nlfsr(R, mask)
            tmp = (tmp << 1) ^ out
        if(tmp!=ans[i]): return
    print(bin(c))

for i in range(2**21):
    if(i%10000==0):print("++",i)
    test(i)

# f=open("key","ab")
# for i in range(1024*1024):
#     tmp=0
#     for j in range(8):
#         (R,out)=nlfsr(R,mask)
#         tmp=(tmp << 1)^out
#     f.write(chr(tmp))
# f.close()
