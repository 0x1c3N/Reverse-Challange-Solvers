pvar2 = [0x42,0x57,0x45,0x4b,0xbb,0xcc,0xcc,0x81,0x7a,0x71,0x66,0x71,0xbb,0xdf,0xcd,0x86,0x6f,0x64,0x5c,0x6e,0xad,0xf2,0xd8,0x9a,0x6f,0x7e]
local_48 = [1,3,3,7,0xde,0xad,0xbe,0xef]
flag = ""
local_54 = 0
while True:
    uVar3 = (local_54 >> 0x1f)>> 0x1d

    flag += chr(pvar2[local_54] ^ local_48[((local_54 + uVar3 & 7) - uVar3)])

    local_54 = local_54 + 1

    if (local_54 == 26):
        break

print(flag)
