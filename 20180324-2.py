# assert flag.startswith("flag{")
# assert flag.endswith("}")
# assert len(flag)==27

def lfsr(R,mask):
    output = (R << 1) & 0xffffff
    i=(R&mask)&0xffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)

ans=[178 ,233 ,14 ,19 ,160 ,106 ,27 ,252 ,64 ,230 ,125 ,83]

def solve(R):
    c=R
    now=[]
    mask = 0x100002
    for i in range(12):
        tmp = 0
        for j in range(8):
            (R, out) = lfsr(R, mask)
            tmp = (tmp << 1) ^ out
        now.append(tmp)
    if(now==ans):print(c)

for i in range(2**21):
#     if(i%10000==0):print("++",i)
    solve(i)
print(bin(1821289))