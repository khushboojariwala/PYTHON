#Write a Python program to find the highest 3 values in a dictionary

data = {'a': 30, 'b': 50, 'c': 20, 'd': 70, 'e': 45}

sorted_values = sorted(data.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_values[:3]

print("Top 3 values in the dictionary:")
for key, value in top_3:
    print(f"{key}: {value}")
