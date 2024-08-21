import math
# print(math.sqrt(49))


"""
Program should be able to handle edge cases

For Q1 here are few edge cases
1. The number is somewhere in middle of the list
2. The number is at the beginning of the list
3. The number is at the end of the list
4. The list is empty
5. The list contains only one element / and it is the number expected
6. The list does not contain the number
7. The list contains duplicate numbers
8. The number is present multiple times in the list
etc.

"""

"""
Q.1
We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

Here the simplest solutions is brute force
1. Create a variable index with the value O.
2. Check whether the number at index index in card equals number .
3. If it does, index is the answer and can be returned from the function
4. If not, increment the value of index by 1, and repeat steps 2 to 5 till we reach the last
index.
5. If the number was not found, return —1 .

"""

# cards = [1,2,3,4,5,6,7,8,0,9]
cards =[]
number = 0
answer = 8




def find_number(cards,number):
    index = 0
    print("cards",cards)
    print("number",number)


    """having while loop true can solve the problem that has some elements to check,
    in order to solve the case where list is empty -> condition needs to be changed
    so set it to check for the index we are trying to access should be less then the length of list, hence no element means no length and it gives the false as result
    """
    while index < len(cards):
        print("index",index)
        if cards[index] == number:
            return index 
        index +=1
        if index == len(cards):
            return -1
        

result = find_number(cards,number)

if result == answer :
    print("True")
else:
    print("False")

