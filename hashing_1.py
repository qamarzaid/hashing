
size=int(input("enter size"))
h_ash=["_"]* size

for i in range(0,size):
    ele=int(input("enter entry ; "))
    if ele>0:
        M = ele % size
        h_ash[M]=ele 
        #print(M)
    else:
        pass 

print(h_ash)
'''
print("-----HASH TABLE-----")
print("|   INDEX | Entry   | ")
for i in range (0,size):
     print("|",i,"|" ,h_ash[i], "| ")
     print("--------------------")
'''
