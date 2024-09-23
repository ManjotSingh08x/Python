from random import choice

digit_list = [1,2,3,4,5,6,7,8,9,0,'A','B','C','D','E']

def generate_result(digit_list):
    result=''
    for i in range(4):
        result+= str(choice(digit_list))
    return result

my_ticket = '0CDE'

counter = 0
while True:
    result = generate_result(digit_list)
    print(result)
    counter += 1
    if result == my_ticket:
        print("You won!!")
        print(f"The loop ran {counter} times")
        break
    