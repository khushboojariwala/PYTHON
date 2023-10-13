"""
5-What is the purpose continue statement in python?
    In Python, the continue statement is used to control the    flow of a loop, such as a for or while loop. When continue is encountered within a loop, it causes the current iteration to be prematurely terminated, and the loop then proceeds to the next iteration. In other words, it skips the remaining code within the current iteration and continues with the next iteration.

    The primary purpose of the continue statement is to     selectively skip specific iterations of a loop based on a certain condition. It is often used when you want to avoid executing a part of the loop's code under certain conditions, but still, continue with the next iteration of the loop.

"""
#Example :
     
for num in range(1,11):
    if num == 2:
        continue
    print(num)