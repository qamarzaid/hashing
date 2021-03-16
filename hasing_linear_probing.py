
size=int(input("enter size"))
h_ash=["_"]* size

for i in range(0,size):
    ele=int(input("enter entry ; "))
    if ele>0:
        M = ele % size
        if h_ash[M]=="_":
        	h_ash[M]=ele
        else:
        	N=M
        	i=0
        	while h_ash[N]!="_":
        		N=(M+i)%size
        		i=i+1
        		h_ash[N]=ele
    else:
        pass
print(h_ash)
print("-----HASH TABLE-----")
print("|   INDEX | Entry   | ")
for i in range (0,size):
     print("|",i,"|" ,h_ash[i], "| ")
     print("--------------------")
