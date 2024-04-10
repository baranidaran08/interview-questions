
#How do you access the third element of a list?
# print(list1[2])


#Write a function to find the maximum element in a list.
# def find_max(list1):
#     if not list1:
#         return None
#     return max(list1)

list1=[2,4,6,8,10]
# print(find_max(list1))

#another way
# max = list1[0]
# for x in list1:
#     if x > max:
#         max=x
# print(max)

#How do you add an element to the end of a list?
# list1.append(12)
# print(list1)


#Write a Python program to remove duplicates from a list.
# unique_list = []
# for x in list1:
#     if x not in unique_list:
#         unique_list.append(x)
# print(unique_list)


#Write a function to check if a given list is empty or not.
# def my_function(list1):
#     if list1 is None:
#         print("the given list is none")
#     else:
#         print("it has elements")


# list1=[2,4,6,8,10]
# my_function(list1)


#How do you sort a list in descending order?
# sorted_list = sorted(list1,reverse=True)
# print(sorted_list)


#Write a program to concatenate two lists in Python.
# list2=[1,3,5,7,9]
# list1.extend(list2)
# print(list1)






###############################################################

my_tuple=(1,2,3,4,5)
#Write a Python program to reverse a tuple.
# a=my_tuple[::-1]
# print(a)


#Write a function to find the index of a given element in a tuple.
# element = 5

# index = ()
# for i in range(len(my_tuple)):
#     if my_tuple[i] == element:
#         index = i
# print(index)

#another way
# a =my_tuple.index(element)
# print(a)

#Explain the concept of tuple unpacking in Python.
# a,b,c,d,e,=my_tuple
# print(a,b,c,d,e)

#How do you convert a tuple to a list
# a = list((my_tuple))
# print(a)

#Write a program to concatenate two tuples in Python.
# def my_function(my_tuple,t2):
#     return my_tuple + t2

# my_tuple=(1,2,3,4,5)
# t2=(6,7,8,9,10)

# print(my_function(my_tuple,t2))

#How do you create a tuple with a single element?
# single_element = (3,)
# print(single_element)


#Write a Python program to convert a tuple to a string
# a = ('H','E','L','L','O')#tuple to string
# b = ''.join(a)
# print(b).

#####################################################################

set1={2,3,4,5}

#Write a Python program to create an empty set.
# empty_set={}
# print(empty_set)

#How do you add an element to a set?
# set1.add(4)
# print(set1)

#Write a function to find the intersection of two sets.
# set2={3,4,5}

# a=set()

# for x in set1:                   #?
#     if x in set2:
#         a.add(x)
# print(a)


#Write a program to check if a given element exists in a set.
# my_set = {1, 2, 3}
# element = 2
# if element in my_set:
#     print("Element exists in the set")
# else:
#     print("Element does not exist in the set")

#How do you remove an element from a set?
# set1.remove(2)
# print(set1)


#Write a Python program to remove all duplicate elements from a given set
# set2={2,3,4,4,4,5,5,6,6,7,8}

# a=set()
# for x in set2:
#     if x not in a:
#         a.add(x)

# print(a)

#another way
# set2={2,3,4,4,4,5,5,6,6,7,8}
# unique_set = set(set2)  #it automatically removes duplicates
# print(unique_set)

#############################################################################

#Write a Python program to create an empty dictionary.
# dict1= dict()
# print(dict1)


#How do you access the value associated with a specific key in a dictionary?
dict1={'a':1,'b':2,'c':3,'d':4}
# for x in dict1.values():
#     print(x)


#Write a function to check if a key exists in a dictionary.
# def my_function(dict1,key):
#         if key in dict1:
#             return ("key is present")
#         else:
#             return ("key is not present")
        
# dict1={'a':1,'b':2,'c':3,'d':4}
# key='k'
# print(my_function(dict1,key))



#How do you add a new key-value pair to a dictionary?
# dict1['e'] = 4
# print(dict1)


#Write a program to iterate through all key-value pairs in a dictionary.
# for k,v in dict1.items():
#     print(k,v)



#How do you remove a key-value pair from a dictionary?
# dict1.pop('a')
# print(dict1)

#Write a Python program to merge two dictionaries.
# dict2={'e':5,'f':6,'g':7}
# dict1.update(dict2)
# print(dict1)


##################################################################################

#Define a function that takes two parameters and returns their sum.
# def my_function(a,b):
#     return a+b

# sum=my_function(20,40)
# print(sum)


#Write a function to find the factorial of a given number.
# def my_function(fact):
#     if fact==0:
#         return 1
#     else:
#         return fact * my_function(fact-1)
    
# fact=5
# result=my_function(fact)
# print(result)



#Write a Python function to check if a given number is prime.

# If given number is greater than 1

def my_function(num):
    if num > 1:
    # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return f"{num} is not a prime number"
                break                  
        else:
            return f"{num} is a prime number"
    else:
        return f"{num} is not a prime number"

num=int(input("enter a number"))
print(my_function(num))
print("finally you have founded your prime number")






