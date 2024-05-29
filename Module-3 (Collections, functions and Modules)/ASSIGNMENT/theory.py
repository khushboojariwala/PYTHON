"""
1.What is List? How will you reverse a list?
-> In Python, a list is a built-in data structure that can hold a
   collection of items. Lists are ordered, mutable (you can change their contents), and can contain elements of different data types. Lists are created by enclosing a comma-separated sequence of items within square brackets []. For example:
      my_list=[1,2,3,4,5]
   
   To reverse a list in Python, you can use one of the following methods:
   
   1.Using the reverse() method:
     You can use the reverse() method of the list to reverse it in place.
     my_list=[1,2,3,4,5]
     my_list.reverse()
     print(my_list)
   
   2.Using slicing:
     You can also create a reversed copy of the list using slicing. This doesn't modify the original list but returns a new reversed list.
     my_list=[1,2,3,4,5]
     reversed_list=my_list[::-1]
     print(reversed_list)
   
   3.Using the reversed() function:
     The reversed() function returns a reverse iterator, which you can convert into a list: 
     my_list=[1,2,3,4,5]
     reversed_list=list(reversed(my_list))
     print(reversed_list) 
   
2.How will you remove last object from a list?
Suppose list1 is [2, 33, 222, 14, and 25], 
what is list1 [-1]? 
-> Using the pop() method:
    You can use the pop() method with the index of -1 to remove the last element from the list. The pop() method also returns the removed element, so you can assign it to a variable if you need to capture the removed value.

    list1 = [2, 33, 222, 14, 25]
    last_element = list1.pop(-1)
    print(list1)                    # Output: [2, 33, 222, 14]
    print(last_element)             # Output: 25

->what is list1 [-1]? 
    If list1 is [2, 33, 222, 14, 25],then list1[-1] will give you 25, which is the last element in the  list.

3.Differentiate between append () and extend () methods?
-> In Python, both append() and extend() are list methods used add  elements to a list, but they work differently and have distinct purposes.

append() method:

    append() is used to add a single element to the end of a list.
    It takes one argument, which is the element you want to add to the list.After using append(), the list will have one additional element at the end.If you pass a list as an argument to append(), the entire list will be added as a single element at the end of the original list.
    Example using append():

    my_list = [1, 2, 3]
    my_list.append(4)  # Adds a single element
    print(my_list)  # Output: [1, 2, 3, 4]
    
extend() method:
    
    extend() is used to add multiple elements (from an iterable, like a list or a tuple) to the end of a list.
    It takes an iterable (e.g.a list, tuple, or string) as an argument and adds each element from the iterable to the end of the list.
    After using extend(), the list will be extended with the elements from the iterable.
    Example using extend():

    my_list = [1, 2, 3]
    my_list.extend([4, 5])  # Adds multiple elements
    print(my_list)  # Output: [1, 2, 3, 4, 5]
    
    my_list = [1, 2, 3]
    my_list.extend("abc")  # Adds elements from a string
    print(my_list)  # Output: [1, 2, 3, 'a', 'b', 'c']
    
    In summary, append() adds a single element to the end of the list, while extend() adds multiple elements from an iterable to the end of the list. 
    
18.What is tuple? Difference between list and tuple.
->A tuple in Python is a data structure that is similar to a list, but it is immutable, meaning its contents cannot be changed after creation. Tuples are defined by enclosing elements in parentheses () and separated by commas. For example:
  
   my_tuple=(1,2,3,4)

The key differences between lists and tuples are:

   Mutability: Lists are mutable, meaning you can change, add, or remove elements after the list is created. Tuples, on the other hand, are immutable, so once a tuple is created, you cannot modify its elements. You can create a new tuple by concatenating or slicing existing tuples, but you cannot change the elements within a tuple.

   Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses ().

   Performance: Tuples are generally more memory-efficient and faster than lists, especially when iterating through elements or when used as keys in dictionaries. This is due to their immutability, which allows for certain optimizations in memory allocation and performance.

   Use Cases: Lists are often used when you need a collection of items that may change or evolve over time. Tuples are suitable for situations where you want to store a fixed collection of elements that shouldn't be modified accidentally. Tuples are also used for returning multiple values from functions.

43.Why Do You Use the Zip () Method in Python?
->The zip() function in Python is used to combine multiple iterables (such as lists, tuples, etc.) element-wise. It aggregates elements from each iterable into tuples until the shortest iterable is exhausted. It's often used in scenarios where you want to work with corresponding elements from different collections simultaneously.

  1.Iterating Through Multiple Lists Simultaneously:
    You can loop through multiple lists simultaneously by using zip() to pair elements at corresponding indices.

    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    for num, letter in zip(list1, list2):
        print(num, letter)

  2.Combining Data into Tuples or Dictionaries:
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    
    combined_tuples = list(zip(keys, values))
    print(combined_tuples)
    
    combined_dict = dict(zip(keys, values))
    print(combined_dict)

    
  




   """