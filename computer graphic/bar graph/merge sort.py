import turtle
import random
import time

def draw_bar_graph(data):
    scr = turtle.Screen()
    scr.bgcolor("white")
    scr.tracer(0)
    t=turtle.Turtle()
    t.color("black")
    t.shape("circle")
    t.speed(0)
    t.pensize(3)
    t.penup()
    t.setpos(50-1*(scr._window_size()[0]/2),50-(scr._window_size()[1]/2))
    t.pendown()
    for i in range(len(data)):
        t.left(90)
        t.forward(data[i])
        t.right(90)
        t.forward(scr._window_size()[0]/100)
        t.right(90)
        t.forward(data[i])
        t.left(90)
        scr.update()

def merge(left, right):
    # Initialize an empty list to store the merged result
    result = []
    # Initialize two pointers to track the indices of left and right lists
    i = 0 # pointer for left list
    j = 0 # pointer for right list
    # Loop until one of the lists is exhausted
    while i < len(left) and j < len(right):
        # Compare the current elements of left and right lists
        if left[i] <= right[j]:
            # Append the smaller element to the result list
            result.append(left[i])
            # Increment the pointer for left list
            i += 1
        else:
            # Append the larger element to the result list
            result.append(right[j])
            # Increment the pointer for right list
            j += 1
    # Append the remaining elements of the non-exhausted list to the result list
    result += left[i:]
    result += right[j:]
    # Return the merged result list
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    scr.clear()
    draw_bar_graph(merge(left,right))
    time.sleep(0.3)
    return merge(left, right)

data=[random.randint(1,800) for i in range(50)]
scr = turtle.Screen()
merge_sort(data)