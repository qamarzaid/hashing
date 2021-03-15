### Hashing 
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
So here we have tried to create an Array or List of user's desired size  not emepty but it contains "_" which we have assumed as empty spaces.
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
