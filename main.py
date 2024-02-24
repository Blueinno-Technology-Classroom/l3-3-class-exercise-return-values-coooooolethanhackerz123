##################################################
'''
Q1: 
'''

# TODO: Write your code here
def cube_a_number(x):
    result = x * x * x
    return result

cubed_res = cube_a_number(10)
print(f'The result is {cubed_res}.')
##################################################
'''
Q2:
'''

# TODO: Write your code here
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
 
result = is_even(13)    # result => True or False
print(f'13 is even: {result}')
##################################################
'''
Q3:
'''

# TODO: Write your code here
def is_even(n):
    print(n % 2 == 0)
    return n % 2 == 0
    return True
 
result = is_even(12)    # result => True or False
print(f'12 is even: {result}')
##################################################
'''
Challenge:
'''

# TODO: Write your code here
def score_to_gpa(score):
    result = score/100*4
    return round(result,1)

alice_score = score_to_gpa(50)  # 2.0
bob_score = score_to_gpa(90)    # 3.6

print(alice_score,bob_score)
##################################################
