number = int(input("Enter\n"))
lend=len(str(number))
leno=len(str(oct(number)))
lenh=len(str(hex(number)))
lenb=len(str(bin(number)))
print(lenb)
for i in range(1,number+1):
    d = str(i).rjust(lend)
    o = str(oct(i)).rjust(leno)
    h = str(hex(i)).rjust(lenh)
    b = str(bin(i)).rjust(lenb,' ')
    len_b = len(b)-1
    len_o = len(o)-2
    len_h = len(h)-2


    s = ''
    ans=d+s.ljust(abs(len_o-(lenb-2)))+o[2:]+s.ljust(abs(len_h-(lenb-2)))+h.replace('0x','')+s.ljust((len_b)-(lenb-2))+b.replace('0b','')
    print(ans)