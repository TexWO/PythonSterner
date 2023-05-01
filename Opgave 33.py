import random
# 1:

#def Biggest_Num(a,b,c):
    #numbers = [a,b,c]
    #max_num = max(numbers)
    #print(max_num)

#Biggest_Num(1,500,10)

# 2:
#def Largest_num_in_list(*num):
    #num = [*num]
    #Largest_num = max(num)
    #print(Largest_num)

#Largest_num_in_list(500,300,400,1000,766,222)

# 3:
#def switch_num(*num):
    #list1 = [*num]
    #random.shuffle(list1)
    #print(list1)

#switch_num(32,22,11,66,77,99,81)

# 4:
#def Given_interval(number, lowestnumber, largestnumber):
    #if number > lowestnumber and number < largestnumber:
        #print(f"The number {number} is inbetween {lowestnumber} and {largestnumber}")

#Given_interval(10,5,15)


# 5:


# 1: Uden brug af max() function
Numbers = [1, 200, 700, 4000, 5, 6]

Largest_num = Numbers[0]

for number in Numbers:
    if Largest_num < number:
        Largest_num = number

print(Largest_num)