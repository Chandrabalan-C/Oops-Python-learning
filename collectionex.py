#List - [insert, append, extend, pop,del,clear]
# Mutable, Allow Duplicates, Ordered, Any type of data can stored
"""
a = [1,2,3,45,6]
print(type(a))

a.append(7)
print(a)
a.insert(0,3)
print(a)
a[0] = 11
print(a)

c = a.pop(4)
print(a)
print(c)
a.pop()
print(a)

l1 = [1,2,3,4]
l2 = [11,12,13,14]
l1.extend(l2)
print(l1)
"""

#Tuple - (casting(tuple->list),del(whole set))
#Immutable, Allow Duplicates, Ordered, Any type of data can be stored
"""
a = (1,2,3,4,5)
b = list(a)
print(a)
print(b)
b.pop()
c = tuple(b)
del a
print(a)
"""

#Set - {add,remove,pop,del,clear}
#Immutable, No Duplicates, Unordered, Any type of data can be stored
"""
a = {1,2,3,4,5}
print(a)
a.add(12)
a.remove(3)
a.pop()
print(a)
a.pop()
print(a)
"""

#Dictionary - {get,keys,values,items,update,del,clear}
#No Duplicates,Immutable for keys & mutable for values,Any types of data can be stored

a = {
    "name":"Chan",
    "val":"Infinite",
    "no":7,
    "domain":["Business","Product"],
    "age":17
}
print(a)

a["no"] = 5
print(a)
a.update({"no":4})
print(a)

a.pop("age") # del a["age"] or del a
print(a)

a.clear()
print(a)
