# from flag import flag
# assert flag.startswith("flag{")
# assert flag.endswith("}")
# assert len(flag)==25

def lfsr(R,mask):
    output = (R << 1) & 0xffffff
    i=(R&mask)&0xffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)


def solve(R):
    c=R;
    mask = 0b1010011000100011100
    ans=[85 ,56, 247 ,66, 193, 13, 178, 199 ,237 ,224 ,36, 58]
    now=[]
    for i in range(12):
        tmp = 0
        for j in range(8):
            (R, out) = lfsr(R, mask)
            tmp = (tmp << 1) ^ out
        now.append(tmp)
    if(ans==now):print(bin(c))

for i in range(2**19):
    solve(i)

#...01010101
#85 56 247 66 193 13 178 199 237 224 36 58