numbers = [value for value in range(1,10**6 +1)]
print("minimum value is: ", min(numbers))
print("maximum value is: ",max(numbers))
print("sum of numbers from 1 to one million", sum(numbers))
one_mil = 10**6
print("mathematical output: ", one_mil*(one_mil + 1)/2)

odd_list = []
for number in range(1,20,2):
    odd_list.append(number,)
print("list of odd numbers from 1 to 20:")
print(odd_list)

threes_list = []
for number in range(3,31,3):
    threes_list.append(number)
print("list of triples from 3 to 30:")
print(threes_list)

cubes_list1 = []
for number in range(1,11):
    cubes_list1.append(number**3)
print("list of cubes from 1 to 10 using for loop:")
print(cubes_list1)

cubes_list2 = [values**3 for values in range(1,11)]
print("list of cubes using list comprehension:")
print(cubes_list2)