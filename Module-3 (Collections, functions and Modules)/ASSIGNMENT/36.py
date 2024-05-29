#How Do You Check The Presence Of A Key In A Dictionary?

my_dict = {'a': 1, 'b': 2, 'c': 3}
given_key = 'b'

if given_key in my_dict:
    print(f"The key '{given_key}' exists in the dictionary.")
else:
    print(f"The key '{given_key}' does not exist in the dictionary.")
