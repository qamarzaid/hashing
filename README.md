## Hashing 
```
Hashing is an important Data Structure which is designed to use a special function called the 
Hash function which is used to map a given value with a particular key for faster access 
of elements. The efficiency of mapping depends of the efficiency of the hash function used.
```
### Hashing In Python Without Using Dictionary
```
In python for hashing there is built in data type called Dictionary. 
Dictionary is the collection of Key:value pair seperated by comma enclosed curly brackets{}.
E.g. {zaid:boy,mrunal:girl,malika:girl}
In this the zaid, mrunal, malika are the key with the value boy, girl, girl respectively.
So in dictionary the key should be always unique.

But here in this code we are going to try hashing technique and gimplement it without dictionary.
using some hash functions.
```

```
As  python don't aloow or support to initialize an empty array or list of user's choice initially.
So here we have tried to create an Array or List of user's desired size  not emepty but 
it contains "_" which we have assumed as empty spaces.
```
#### E.g.
```python
size=int(input("enter size"))
h_ash=["_"]* size
print(h_ash)
```
##### Input
```
enter size10
```
##### Output
```
["_","_","_","_","_","_","_","_","_","_"]
```
##### Code
```python
size=int(input("enter size"))       #taking input size
h_ash=["_"]* size                   # creating a list of size*("_")

for i in range(0,size):             #iterating troughout the list for taking the input of elements
    ele=int(input("enter entry ; "))    #taking the input of element
    if ele>0:                       # checking the contion if the entery or element is empty or 0
        M = ele % size              # Hash Function used
        h_ash[M]=ele     # alocating  position to the element at the outcome of hash function index 
        
    else:
        pass 

print(h_ash)                        #printing out the list after completion of hashing
```
##### Input
```
enter size10
enter entry ; 56
enter entry ; 78
enter entry ; 93
enter entry ; 45
enter entry ; 12
enter entry ; 0
enter entry ; 0
enter entry ; 74
enter entry ; 67
enter entry ; 0
```
##### Output
```
['_', '_', 12, 93, 74, 45, 56, 67, 78, '_']
```
[Demo code link](https://replit.com/@ZaidQamar/hashing#main.py)

#### Done

### Collision in Hashing
```
While doing hashing when two or more element get the same position this situation occured is called Collision.
There are various method for resolving this situations know as Collision Resolution Technique.
```
#### Collision resolution technique: Linear Probing
```
When collision occurs, then collision can be solved by placing second record linearly down whenever the empty location is found.
```
##### E.g.
```
 Let 12, 44, 58, 21, 48, 51, 22, 91 is to be inserted in hash table.
h(key) = key % table size
h(12) = 12 % 10 = 2 insert at 2nd bucket
h(44) = 44 % 10 = 4 insert at 4th bucket
h(58) = 58 % 10 = 8 insert at 8th bucket
h(21) = 21 % 10 = 1 insert at 1st bucket
h(48) = 48 % 10 = 8 No vacant space at 8th bucket so insert at 9th
h(51) = 51 % 10 = 1 No vacant space at 1st bucket so insert at 3rd
h(22) = 22 % 10 = 2 No vacant space at 2nd bucket so insert at 5th
h(91) = 91 % 10 = 1 No vacant space at 1st bucket so insert at 6
```
##### Code
```python

size=int(input("enter size"))   #taking input size
h_ash=["_"]* size                # creating a list of size*("_")

for i in range(0,size):         #  #iterating troughout the list for taking the input of elements
    ele=int(input("enter entry ; "))     #taking the input of element
    if ele>0:				# checking the contion if the entery or element is empty or 0
        M = ele % size			# Hash Function used
        if h_ash[M]=="_":		# checking the hash function out position in list is empty or not.
		h_ash[M]=ele		# if its empty then alocate element there
	else:				# else
		N=M			
		i=0
		while h_ash[N]!="_":	# iterate in the list till found empty place 
			N=(M+i)%size	#new hash function
			i=i+1
		h_ash[N]=ele		#alocate element there
    else:
        pass
print(h_ash)
```
##### Input
```
enter size10
enter entry ; 12
enter entry ; 44
enter entry ; 58
enter entry ; 21
enter entry ; 48
enter entry ; 51
enter entry ; 22
enter entry ; 91
enter entry ; 0
enter entry ; 0
```
##### Output
```
['_', 21, 12, 51, 44, 22, 91,'_', 58, 48]
```
