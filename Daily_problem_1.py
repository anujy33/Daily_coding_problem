'''
# Problem statement
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''

# Algorith #
# Given : first list
# second: Sum number
# Iterate thru the list twice and keep adding the number and check if sum is equal to input. If yes return true\
#       else continue the loop


####################My first solution #######################
list1 = [10, 15, 3, 7]
k = 27


def add_number_result(a=None, b=None):
    if a:
        for i in a:
            for j in range(len(a)):
                if i + a[j] == b:
                    if i == a[j]:
                        break
                    return True
                else:
                    continue
        return False


check = add_number_result(list1, k)
print(check)

