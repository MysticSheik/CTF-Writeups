# 0 - 69
l1 = marshal.load('c\x02\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00C\x00\x00\x00s\x08\x00\x00\x00|\x00\x00|\x01\x00AS(\x01\x00\x00\x00N(\x00\x00\x00\x00(\x02\x00\x00\x00t\x01\x00\x00\x00at\x01\x00\x00\x00b(\x00\x00\x00\x00(\x00\x00\x00\x00s\x07\x00\x00\x00<stdin>t\x08\x00\x00\x00<lambda>\x01\x00\x00\x00s\x00\x00\x00\x00')
l2 = marshal.load('c\x02\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00C\x00\x00\x00s\x08\x00\x00\x00|\x00\x00|\x01\x00\x17S(\x01\x00\x00\x00N(\x00\x00\x00\x00(\x02\x00\x00\x00t\x01\x00\x00\x00at\x01\x00\x00\x00b(\x00\x00\x00\x00(\x00\x00\x00\x00s\x07\x00\x00\x00<stdin>t\x08\x00\x00\x00<lambda>\x01\x00\x00\x00s\x00\x00\x00\x00')
l3 = marshal.load('c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00C\x00\x00\x00s\x04\x00\x00\x00d\x01\x00S(\x02\x00\x00\x00Nt%\x00\x00\x00Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1A(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x07\x00\x00\x00<stdin>t\x08\x00\x00\x00<lambda>\x01\x00\x00\x00s\x00\x00\x00\x00')
l4 = marshal.load('c\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00C\x00\x00\x00s\x07\x00\x00\x00t\x00\x00\x83\x00\x00S(\x01\x00\x00\x00N(\x01\x00\x00\x00t\t\x00\x00\x00raw_input(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x07\x00\x00\x00<stdin>t\x08\x00\x00\x00<lambda>\x01\x00\x00\x00s\x00\x00\x00\x00')

# 72 - 78
dummy = <code object <lambda> at 0x7f42c16fc8b0, file "chall.py", line 7>

# 81 - 87
dummy.func_code = l4

# 90 - 96
flag = dummy()

# 99 - 102
out = ''

# 105 - 127
for i in range(len(flag)):
    # 130 - 143
    o1 = ord(flag[i])
    
    # 146 - 152
    dummy.func_code = l3
    
    # 155 - 171
    o2 = ord(dummy()[i])
    
    # 174 - 180
    dummy.func_code = l1
    
    # 183 - 195
    o3 = dummy(o1, o2)
    
    # 198 - 204
    dummy.func_code = l2
    
    # 207 - 219
    o4 = dummy(o3, 20)
    
    # 222 - 228
    dummy.func_code = l1
    
    # 231 - 243
    o5 = dummy(o4, 90)
    
    # 246 - 269
    out += chr(o5 XOR 1)

# 270 - 295
open('flag_enc', 'w').write(out)