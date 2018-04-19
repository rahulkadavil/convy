#!/usr/bin/env python
print "Enter the value:"
s =raw_input()
listhex = []
listdec = []
listbin = []
for i in s:
    print "Converter for " +i
    hexa = hex(ord(i))
    listhex.append(hexa)
    listhex.append(":")
    print "Hexadecimal :" + hexa
    inte = int(hexa[2:],16)
    listdec.append(str(inte))
    listdec.append(":")
    print "Decimal :" + str(inte)
    binary = bin(inte)
    listbin.append(binary)
    listbin.append(":")
    print "Binary :" + binary
print "Final hexadecimal- "+"".join(listhex)
print "Final decimal- "+"".join(listdec)
print "Final binary- "+"".join(listbin)
