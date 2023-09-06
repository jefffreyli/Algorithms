import random

# # Question 5
# def separate(s, n):
#     """ s is a str
#         n is a positive int 
    
#     Separates s in consecutive strings of length n, starting from the 
#     beginning of s. If s can be evenly separated, returns a tuple of 
#     the boolean True and the string pieces, in order. If s cannot be 
#     evenly separated, return a tuple of the boolean False and only the 
#     string pieces of length n, in order.
#     """
    
   #  if n <= 0 or len(s) == 0:
   #      return False, ()

   #  result = []
   #  for i in range(0, len(s), n):
   #      result.append(s[i:i+n])

   #  if len(s) % n == 0:
   #      return True, tuple(result)
   #  else:
   #      return False, tuple(result[:-1])

# # For example:
# print(separate("abcd", 1))     # prints (True, 'a', 'b', 'c', 'd')
# print(separate("abcd", 2))     # prints (True, 'ab', 'cd')
# print(separate("abcd", 3))     # prints (False, 'abc')
# print(separate("abcdefg", 2))  # prints (False, 'ab', 'cd', 'ef')




# def separate(s, n):
#     """ s is a str
#         n is a positive int 
    
#     Separates s in consecutive strings of length n, starting from the 
#     beginning of s. If s can be evenly separated, returns a tuple of 
#     the boolean True and the string pieces, in order. If s cannot be 
#     evenly separated, return a tuple of the boolean False and only the 
#     string pieces of length n, in order.
#     """
    
   #  ans = []
   #  for i in range(0, len(s), n):
   #      ans.append(s[i:i+n])

   #  if len(s) % n == 0:
   #      L = []
   #      L.append(True)
   #      L.extend(ans)
   #      return tuple(L)
   #  else:
   #      L = []
   #      L.append(False)
   #      L.extend(ans[:-1])
   #      return tuple(L)
    


# # For example:
# print(separate("abcd", 1))     # prints (True, 'a', 'b', 'c', 'd')
# print(separate("abcd", 2))     # prints (True, 'ab', 'cd')
# print(separate("abcd", 3))     # prints (False, 'abc')
# print(separate("abcdefg", 2))  # prints (False, 'ab', 'cd', 'ef')




# Question 6
def longest_sequence(L, pattern):
    """ L is a list of ints
        pattern is a list of ints
        
    Returns the length of the longest sequence from pattern that is 
    found in L (in the same order). If no such pattern is found, return 0.
    """

    
    
#     copy = pattern[:]
#     found = False

#     while not found:
#         if sublist_exists(L, copy):
#             return len(copy)
#         else:
#             copy.pop()

#     return 0  # If the loop completes without finding the pattern, return 0.

# def sublist_exists(a, b):
#     for i in range(len(a)):
#         if a[i:i+len(b)] == b:
#             return True
#     return False


print(longest_sequence([1,2,3,4], [3]))              # prints 1    
print(longest_sequence([1,2,3,4], [1,2]))            # prints 2
print(longest_sequence([1,2,3,4], [1,2,3,4]))        # prints 4
print(longest_sequence([1,2,3,4,2,3,4,5], [2,3,4]))  # prints 3
print(longest_sequence([1,2,3,2,4], [3,2,1]))        # prints 2
print(longest_sequence([6,8,6,8,6,8,6,8,6,8], [8,8,6,8,6,8,6,8,8])) # prints 7



# # Question 7
# def encrypted_occurring(s, cipher, n):
#     """ s is a string of lowercase alphabetical characters and spaces, 
#             with words being a sequence of non-space characters between spaces.
#         cipher is a dict mapping a str alphabetical character to another str 
#             alphabetical character.
    
#     Applies cipher to each character in s, to create an "encrypted" s. 
#     Returns a list, sorted alphabetically, of all the words in the original 
#     s, whose encrypted version occurs at least n times in the encrypted s.
#     """
    # your code here
   
   #  words = s.split(" ")
   #  encrypted_words = []

   #  for word in words:
   #      e_word = ""
   #      for char in word:
   #          if(char in cipher.keys()):
   #              e_word = e_word + cipher[char]
   #          else:
   #              e_word = e_word + char
   #      encrypted_words.append(e_word)
    
   #  words_with_encrypted_occuring_n = []
   #  for i in range(len(encrypted_words)):
   #      if(encrypted_words.count(encrypted_words[i]) >= n):
   #          words_with_encrypted_occuring_n.append(words[i])
    
   #  return sorted(words_with_encrypted_occuring_n)



   #  words = s.split(" ")
   #  encrypted_words = []
   #  for word in words:
   #      encrypted = ""
   #      for letter in word:
   #          if(letter in cipher.keys()):
   #             encrypted = encrypted + cipher[letter]
   #          else:
   #             encrypted +=letter
   #      encrypted_words.append(encrypted)

   #  ans = []
   #  for i in range(len(words)):
   #      count = encrypted_words.count(encrypted_words[i])
   #      if count >= n and words[i] not in ans:
   #          ans.append(words[i])
   #  return ans

   #  ans = []
   #  index = 0
   #  for word in encrypted_words:
   #      count = 0
   #      for i in encrypted_words:
   #          if(i == word):
   #              count+=1
   #    #   index+=1
   #      if(count == n):
   #         ans.append(words[index])
   #  return ans


    
    
         
        
# s = "abc def"
# d = {'a':'b'}
# print(encrypted_occurring(s, d, 0)) # prints ['abc', 'def']

# s = "abc dbc xy"
# d = {'a':'b', 'd':'b'}
# print(encrypted_occurring(s, d, 1)) # prints ['abc', 'dbc', 'xy']

# s = "abc dbc xy"
# d = {'a':'b', 'd':'b'}
# print(encrypted_occurring(s, d, 2)) # prints ['abc', 'dbc']



# def biggest_pair_true(f, g, n):
#     """ f and g are functions that take in an int and return a bool
#         n is an int > 0
    
#     Consider applying f to ints 0 through n (inclusive) and separately 
#     applying g to ints 0 though n (inclusive). Returns the sum of the 
#     largest int that return True when f is applied to it with the 
#     largest int that returns True when g is applied to it. If there 
#     aren't any pairs of ints that both return True, returns None. 
#     """
    
   #  max_f = -999999
   #  max_g = -999999
   #  for i in range(0, n+1):
   #      if(f(i)):
   #         max_f = max(max_f, i)

    
   #  for i in range(0, n+1):
   #      if(g(i)):
   #         max_g = max(max_g, i)
    
   #  if max_f == -999999 or max_g == -999999:
   #      return None
    
   #  return (max_f + max_g)
      

# # For example:
# print(biggest_pair_true(lambda x:True, lambda x:True, 5))  # prints 10
# print(biggest_pair_true(lambda x:True, lambda x:False, 10))  # prints None
# print(biggest_pair_true(lambda x:x%2==0, lambda x:x%4==0, 10))  # prints 18





# # Question 10
# flattened = []
# def flatten(L):    
#     for i in L:
#         if(isinstance(i, list)):
#             flatten(i)
#         else:
#             flattened.append(i)
#     return flattened

# def count_lengths(LL):
#     arr = flatten(LL)
#     total = 0

#     for i in arr:
#         if(isinstance(i, str)):
#             total = total + len(i)
#         else:
#             raise ValueError
      
#     return total


# #Question 11
# class Employee():
#     """ An employee with an employee number and a salary data attributes """
#     def __init__(self, n, s=50000):
#         """ Initializes an Employee object with 
#         * n, an integer employee number (does not need to be unique)
#         * s, an integer salary -- salary defaults to 50000 if not specified. """
#         self.employee_number = n
#         self.salary = s
#         pass
#     def set_salary(self, s):
#         """ Sets the employee salary to integer s """
#         self.salary = s
        
#     def get_salary(self):
#         """ Returns the employee salary """
#         return self.salary
        
#     def get_n(self):
#         """ Returns the employee number """
#         return self.employee_number
        
#     def __str__(self):
#         """ Returns the string representation of the employee number """
#         return str(self.employee_number)
        
    
# # For example    
# e1 = Employee(1)        
# print(e1)              # prints 1
# print(e1.get_salary()) # prints 50000

# e2 = Employee(2)        
# e2.set_salary(60000)
# print(e2)              # prints 2
# print(e2.get_salary()) # prints 60000

    

# #Question 12
# class Manager(Employee):
#     """ A subclass of Employee. """
#     def __init__(self, n):
#         """ Initializes the manager with data attributes: 
#         * employee number n
#         * salary of 70000 
#         * a list of Employee objects working under self, initially empty """
#         Employee.__init__(self, n, 70000)
#         self.employees = []
        
#     def add_worker(self, e):
#         """ e is an Employee, not Manager, object
#         Adds e to its list of employees working under self only if there is no 
#         other employee in the list with the same employee number already. 
#         Otherwise does nothing. """
#         employee_numbers = []
#         for i in self.employees:
#             employee_numbers.append(i.get_n())
         
#         if not e.get_n() in employee_numbers:
#             self.employees.append(e)
        
        
#     def get_employees_under(self):
#         """ Returns a copy of the list containing all Employee objects 
#         working under self, in any order """
#         copy = self.employees[:]
#         return copy
                
#     def get_employee_numbers_under(self):
#         """ Returns a list (sorted in ascending order) containing 
#         the integer values for all employees numbers working under self """

#         employee_numbers = []
#         for i in self.employees:
#             employee_numbers.append(i.get_n())
        
#         return sorted(employee_numbers)
        
    
# # For example 
# e1 = Employee(1)        
# e2 = Employee(2)   
# e3 = Employee(1)     

# m1 = Manager(3)
# print(m1)               # prints 3
# print(m1.get_salary())  # prints 70000

# m1.add_worker(e2) 
# print(m1.get_employee_numbers_under())  # prints [2]

# m1.add_worker(e1)
# m1.add_worker(e3)
# print(m1.get_employee_numbers_under()) # prints [1, 2]

# under = m1.get_employees_under()
# print(isinstance(under[0], Employee))  # prints True


# # Question 13
# def payday(L):
#     """ L is a list of Manager objects. Each Manager has one or more 
#     Employees working under them. An Employee only has one Manager. 

#     Returns the sum of all salaries to be paid for Manager objects in L
#     and all Employee objects each Manager in L has.   """
    
#     total = 0
#     for m in L:
#         total = total + m.get_salary()
#         for e in m.get_employees_under():
#             total = total + e.get_salary()
    
#     return total
    

# # For example 
# m1 = Manager(6)
# m1.add_worker(Employee(1))
# m1.add_worker(Employee(2))

# m2 = Manager(7)
# m2.add_worker(Employee(3))

# print(payday([m1,m2]))  # prints 290000 (3 employees and 2 managers)






# def check_all_immutable(LL):
#     """ LL is a list whose elements are lists
    
#     Mutates LL to replace each list in LL with True or False. 
#     A list inside LL is replaced with True if all elements within that list 
#     could be valid Python dict keys. Otherwise, if there is at least one 
#     element within that list that cannot be a valid dict key, that list 
#     is replaced with False. Function returns None.
#     """
    
#     bool_arr = []
#     for L in LL:
#         ok = True
#         for item in L:
#             if(isinstance(item, list) or isinstance(item, dict)):
#                ok = False
#         bool_arr.append(ok)
        
#     LL.clear()
#     for b in bool_arr:
#       LL.append(b)
#     return None

#    #  bool_arr = []
#    #  for L in LL:
#    #      ok = False
#    #      for item in L:
#    #          if(isinstance(item, list) or isinstance(item, dict)):
#    #             ok = False
#    #          else:
#    #             ok = True
#    #      bool_arr.append(ok)
        
#    #  LL.clear()
#    #  for b in bool_arr:
#    #    LL.append(b)
#    #  return LL

# # For example: 
# L = [[2,5,4], ['a',2], [(1,2), [1,2]], [{1:1, 2:2}]]
# check_all_immutable(L)
# print(L)    # L is mutated to [True, True, False, False]

# L = [['a'], [6], [(6,)]]
# check_all_immutable(L)
# print(L)    # L is mutated to [True, True, True]

# L = [[[]], [{'a':1,'b':2}]]
# check_all_immutable(L)
# print(L)    # L is mutated to [False, False]