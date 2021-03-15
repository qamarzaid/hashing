## Hashing 
```
Hashing is an important Data Structure which is designed to use a special function called the 
Hash function which is used to map a given value with a particular key for faster access of elements. 
The efficiency of mapping depends of the efficiency of the hash function used.
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
        h_ash[M]=ele                # alocating  position to the element at the outcome of hash function index 
        
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

