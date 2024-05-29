"""

14-> What are negative indexes and why are they used?
    Negative indexes in programming, particularly in languages like Python and some others, allow you to access elements from the end of a sequence, like a list or a string, rather than the beginning. They are used for several purposes:

    [1]Reverse Access: 
        Negative indexes provide a convenient way to access elements in reverse order. For instance, -1 represents the last element, -2 the second-to-last, and so on. This is useful when you want to iterate through a sequence in reverse.

    [2]Handling Unknown or Variable Lengths: 
        Negative indexes are handy when you don't know the exact length of a sequence, but you need to access elements relative to the end. For example, when working with strings, you might want to get the last character, regardless of the string's length. Using -1 makes this easy.

    [3]Slicing: 
        Negative indexes can be used with slicing to extract elements from the end of a sequence. For example, if you want to extract the last three elements of a list, you can do my_list[-3:].

    [4]Circular Access: 
        In some cases, negative indexes are used to create a circular effect when dealing with sequences. For instance, if you have a list of days and you want to find the day that's two days before Sunday, you can use a negative index -2.

    Example:

    my_list = [1, 2, 3, 4, 5]
    print(my_list[-1])  
    print(my_list[-2])  

    my_string = "Hello, World!"
    print(my_string[-1]) 
    print(my_string[-4:])

    Negative indexes are a useful feature in programming, particularly when you need to work with elements near the end of a sequence or when the sequence's length is not known in advance. They simplify access and manipulation of data in various situations.

"""




