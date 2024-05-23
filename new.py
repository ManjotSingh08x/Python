
def line_repeater(input):
        print(input)
try:       
    answer = int(input("enter a number: "))
    line_repeater(answer)
    for i in range(answer):
        print(f'this number is {i+1}')
    
        
except: 
    print("Do not enter any invalid input")


    
