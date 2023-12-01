#6.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def count_strings(chars):
    count = 0
    for word in chars:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

# Example:
words_list = ['aba', 'xyz', 'aai', 'bcb', 'hello', 'radar']
result = count_strings(words_list)
print(f"The number of strings where the first and last character are the same: {result}")
