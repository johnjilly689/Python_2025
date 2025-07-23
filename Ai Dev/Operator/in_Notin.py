#in: in 	Returns True if a sequence with the specified value is present in the object	x in y	
#not in	Returns True if a sequence with the specified value is not present in the object	
x=['apple','ball']
y=['ball','cat']
print(y in x)
print (x in y)
y.append(x)  #Note x in y only checks if x has y as a element, here x is a element of y. instead of x if you add apple in y then also x in y will give you false because x in why means x should be a fully element of y , not a string or other data type. check the below code also
# y.append("apple") instead of y.append(x)
print(y)
print(x in y)