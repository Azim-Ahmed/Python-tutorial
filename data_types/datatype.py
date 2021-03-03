# In python, everything is an object
name = "Azim"
a = 0 
m = 1.0
c = 1+5j # in python we use complex number in j
b  = True

#these all are base data type
print(type(name))
print(type(a))
print(type(m))
print(type(c))
print(type(b))

#output
# <class 'str'>
# <class 'int'>    
# <class 'float'>  
# <class 'complex'>
# <class 'bool'>


#declaring list with [] this
# list = []
# set = {}
# tuple = () # we must provide at least 2 types of thins. we cannot empty this () bc of we execue this in various way .
#Dict = {'name':'Azim Ahmed', "age":'23'} # this looks like js object

li = [1, 11, 1,1]
z = {1, 1, 2, 3}
t = (1,1,1,1)
d={'name':'Azim Ahmed', "age":'23'}
print(type(li))
print(type(z))
print(type(t))
print(type(d))

#Output
# <class 'list'>
# <class 'set'>
# <class 'tuple'>
# <class 'dict'>

# Python is dynamically strongly typed language
# that would not override the datatype as like as JS. 

n =10 
print("TEST" + n)
# you will get error

# You have to change the datatype by yourself
print("TEST" + str(n)) # that will execute