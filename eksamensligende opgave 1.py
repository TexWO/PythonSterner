#def print_numbers(type='even', n = 10):
    #if type == 'even':
        #for i in range(0, n+1, 2):
            #print(i, end=' ')
    #else:
        #for i in range(1, n+1, 2):
            #print(i, end=' ')


#print_numbers()


import turtle
import random

def draw_random_circles(n):
    turtle.speed('fastest')
    turtle.hideturtle()
    turtle.colormode(255)
    
    for i in range(n):
        radius = random.randint(10, 100)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pencolor(r, g, b)
        turtle.fillcolor(r, g, b)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        
    turtle.done()


print("How many random circles would you like: ")
howManyCircles = input()

draw_random_circles(int(howManyCircles))
