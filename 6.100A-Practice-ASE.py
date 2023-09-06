# https://introcomp.mit.edu/6.100A_ase/MQs/1_MQ1

import random 

# # Question 1.
# # Ans: 1, 6, 10, 12, 13

# x = "pi"
# y = "pie"

# x, y = y, x

# print("x: " + x)
# print("y: " + y)



# def f(x):
#     while x > 3:
#        f(x+1)

# f(1)

# # Question 4.
# def convert_to_mandarin(us_num):
#     """ us_num, a string representing a US number 0 to 99
#     Returns the string mandarin representation of us_num
#     """
#     trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si','5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
#     int_us_num = int(us_num)
#     if(int_us_num <= 10):
#         return trans[us_num]
#     elif(int_us_num >= 11 and int_us_num <= 19):
#         return "shi " + trans[us_num[1:]]
#     else:
#         mando = trans[us_num[0:1]] + " shi"
#         if(us_num[1:] == "0"):
#             return mando
#         else:
#             mando = mando + " " + trans[us_num[1:]]
#             return mando

# # Example Usage
# print(convert_to_mandarin('36')) # will return san shi liu
# print(convert_to_mandarin('20')) # will return er shi
# print(convert_to_mandarin('50')) # will return shi liu

# # Question 5
# def longest_run(L):
#     #increasing
#     start_increasing = 0
#     max_start_increasing = 0
#     end_increasing = 0
#     max_end_increasing = 0
#     diff_increasing = 0
#     longest_increasing_run_sum = 0
    
#     for i in range(len(L)-1):
#       if(L[i+1] >= L[i]):
#          end_increasing=(i+1)
#       else:
#          if(end_increasing - start_increasing + 1 > diff_increasing):
#             diff_increasing = max(end_increasing - start_increasing + 1, diff_increasing)
#             max_start_increasing = start_increasing
#             max_end_increasing = end_increasing
#          start_increasing = i+1
#          end_increasing = i+1
      
#       longest_increasing_run_sum = sum(L[max_start_increasing: max_end_increasing+1])



#     start_decreasing = 0
#     max_start_decreasing = 0
#     end_decreasing = 0
#     max_end_decreasing = 0
#     diff_decreasing = 0
#     longest_decreasing_run_sum = 0
    
#     for i in range(len(L)-1):
#       if(L[i+1] <= L[i]):
#          end_decreasing=(i+1)
#       else:
#          if(end_decreasing - start_decreasing + 1 > diff_decreasing):
#             diff_decreasing = max(end_decreasing - start_decreasing + 1, diff_decreasing)
#             max_start_decreasing = start_decreasing
#             max_end_decreasing = end_decreasing

#          start_decreasing = i+1
#          end_decreasing = i+1
      
#       longest_decreasing_run_sum = sum(L[max_start_decreasing: max_end_decreasing+1])


#       if(diff_increasing > diff_decreasing):
#          return longest_increasing_run_sum
#       elif(diff_increasing < diff_decreasing):
#          return longest_decreasing_run_sum
#       else:
#          return longest_increasing_run_sum if start_increasing < start_decreasing else longest_decreasing_run_sum
            

# a = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# b = [random.randint(0, 15) for i in range(10)]
# c = [1,2,3,4,5,6,7,8,9]
# print(longest_run(c))


# # Question 6
# def general_poly(L):
#     """ L, a list of numbers (n0, n1, n2, ... nk)
#     Returns a function, which when applied to a value x, returns the value: 
#     n0 * x**k + n1 * x**(k-1) + ... nk * x**0 """
    
#     def func(x):
#         exponent_count = len(L) - 1
#         num = 0
#         for digit in L:
#             num = num + digit*(x**exponent_count)
#             exponent_count-=1
#         return num
    
#     return func

# print("Question 6")
# print(general_poly([1, 2, 3, 4])(3))

# #Question 7
# def closest_power(base, num):
#     """ base: base of the exponential, integer > 1
#         num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.
#     """
#     # Your code here
    
#     a, b = 0, 0
#     for i in range(0, num):
#         if(base**i >= num):
#             a = base**i
#             b = base**(i-1)
#             if(abs(num - a) < abs(num - b)):
#                 return i
#             else:
#                 return i-1
#     return 0

# print("Question 6.")
# print(closest_power(3,12)) # returns 2
# print(closest_power(4,12)) # returns 2
# print(closest_power(4,1)) # returns 0


# #Question 8.
# def deep_reverse(L):
#     """ assumes L is a list of lists whose elements are ints
#     Mutates L such that it reverses its elements and also 
#     reverses the order of the int elements in every element of L. 
#     It does not return anything.
#     """
#     # Your code here

#     L.reverse()
#     for lst in L:
#         lst.reverse()

# # For example:
# La = [[1, 2], [3, 4], [5, 6, 7]] 
# deep_reverse(La)
# print(La)  # mutates La to be [[7, 6, 5], [4, 3], [2, 1]]


# # Question 9.
# def f(a, b):
#     return a > b

# def dict_interdiff(d1, d2):
#     """
#     d1, d2: dicts whose keys and values are integers
#     Returns a tuple of dictionaries according to the instructions above
#     """
#     inter = {}
#     diff = {}

#     common_keys = []
#     for i in d1.keys():
#         if(i in d2.keys()):
#             common_keys.append(i)

#     for i in d2.keys():
#         if(i in d1.keys() and not i in common_keys):
#             common_keys.append(i)

#     for key in common_keys:
#         inter[key] = f(d1[key], d2[key])

#     # diff
#     for i in d1.keys():
#         if(not i in d2.keys()):
#             diff[i] = d1[i]

#     for i in d2.keys():
#         if(not i in d1.keys()):
#             diff[i] = d2[i]
    
#     print(inter)
#     print(diff)
#     return (inter, diff)



# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# d3 = {1:30, 2:20, 3:30}
# d4 = {1:40, 2:50, 3:60}

# print(dict_interdiff(d1, d2))
# print(dict_interdiff(d3, d4))


# # Question 10
# def applyF_filterG(L, f, g):
#     """
#     Assumes L is a list of integers
#     Assume functions f and g are defined for you. 
#     f takes in an integer, applies a function, returns another integer 
#     g takes in an integer, applies a Boolean function, 
#         returns either True or False
#     Mutates L such that, for each element i originally in L, L contains  
#         i if g(f(i)) returns True, and no other elements
#     Returns the largest element in the mutated L or -1 if the list is empty
#     """

#     C = L[:]
#     for i in C:
#         if( (g(f(i))) == False):
#             L.remove(i)
#     L[:] = [i for i in L if g(f(i))]
    
#     if(len(L) == 0):
#         return -1
#     else:
#         return max(L)

# # For example:
# def f(i):
#     return i + 2
# def g(i):
#     return i > 5

# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))   # prints 6
# print(L)  # prints [5, 6]

# #Question 11
# flattened = []
# def flatten(aList):
#     """
#     aList: a list 
#     Returns a copy of aList, which is a flattened version of aList  """
    
    
#     for i in aList:
#         if(isinstance(i, list)):
#             flatten(i)
#         else:
#             flattened.append(i)
#     return flattened


# unflattened_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# print(flatten(unflattened_list))



# # Question 12
# ## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
# class Person(object):
#     def __init__(self, name):
#         #create a person with name name
#         self.name = name
#         try:
#             firstBlank = name.rindex(' ')
#             self.lastName = name[firstBlank+1:]
#         except:
#             self.lastName = name
#         self.age = None
#     def getLastName(self):
#         #return self's last name
#         return self.lastName
#     def setAge(self, age):
#         #assumes age is an int greater than 0
#         #sets self's age to age (in years)
#         self.age = age
#     def getAge(self):
#         #assumes that self's age has been set
#         #returns self's current age in years
#         if self.age == None:
#             raise ValueError
#         return self.age
#     def __lt__(self, other):
#         #return True if self's name is lexicographically less
#         #than other's name, and False otherwise
#         if self.lastName == other.lastName:
#             return self.name < other.name
#         return self.lastName < other.lastName
#     def __str__(self):
#         #return self's name
#         return self.name
        
# class USResident(Person):
#     """ 
#     A Person who resides in the US.
#     """
#     def __init__(self, name, status):
#         """ 
#         Initializes a Person object. A USResident object inherits 
#         from Person and has one additional attribute:
#         status: a string, one of "citizen", "legal_resident", "illegal_resident"
#         Raises a ValueError if status is not one of those 3 strings
#         """
#         Person.__init__(self, name)
#         if status not in ["citizen", "legal_resident", "illegal_resident"]:
#             raise ValueError("Invalid status")
        
#         self.status = status
        
        
#     def getStatus(self):
#         """
#         Returns the status
#         """
#         return self.status

# # For example:
# a = USResident('Tim Beaver', 'citizen')
# print(a.getStatus())    # prints citizen
# b = USResident('Tim Horton', 'non-resident')  # will show that a ValueError was raised



# # Question 13a

# class ArrogantProfessor(Professor):
#     def say(self, stuff): 
#         return 'It is obvious that ' + Person.say(stuff) # change self to Person

# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
#     def lecture(self, stuff):
#         return 'It is obvious that ' + Person.say(self, stuff)

# # Question 13b
# class Person(object):     
#     def __init__(self, name):         
#         self.name = name     
#     def say(self, stuff):         
#         return self.name + ' says: ' + stuff     
#     def __str__(self):         
#         return self.name  
    
# class Lecturer(Person):     
#     def lecture(self, stuff):         
#         return 'I believe that ' + Person.say(self, stuff)  
    
# class Professor(Lecturer): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + self.lecture(stuff)
    
# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + 'It is obvious that ' + Lecturer.say(self, stuff)
#     def lecture(self, stuff):
#         return 'It is obvious that ' + Lecturer.lecture(self, stuff)

# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + 'It is obvious that ' + Lecturer.lecture(self, stuff)
#     def lecture(self, stuff):
#         return 'It is obvious that ' + Lecturer.lecture(self, stuff)

# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + 'It is obvious that I believe that ' + self.name + " says: " + stuff
#     def lecture(self, stuff):
#         return 'It is obvious that ' + Lecturer.lecture(self, stuff)

# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + self.lecture(stuff)
#     def lecture(self, stuff):
#         return 'It is obvious that ' + Lecturer.lecture(self, stuff)



# # Question 13 c
# class Person(object):
#     def __init__(self, name):         
#         self.name = name     
#     def say(self, stuff):         
#         return self.name + ' says: ' + stuff     
#     def __str__(self):         
#         return self.name  

# class Lecturer(Person):     
#     def lecture(self, stuff):
#         return 'I believe that ' + Person.say(self, stuff)  

# class Professor(Lecturer): 
#     def say(self, stuff):
#         return "Prof. " + self.name + ' says: ' + self.lecture(stuff)

# class ArrogantProfessor(Professor): 
#     def say(self, stuff):
#         return 'Prof. ' + self.name + ' says: ' + 'It is obvious that ' + Lecturer.say(self, stuff)