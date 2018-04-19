print "Enter the value:"
s =raw_input()
for i in s:
    print "Converter for " +i
    hexa = hex(ord(i))
    print "Hexadecimal :" + hexa
    inte = int(hexa[2:],16)
    print "Decimal :" + str(inte)
    binary = bin(inte)
    print "Binary :" + binary
    print " "
    
