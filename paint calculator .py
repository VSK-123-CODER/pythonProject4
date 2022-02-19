#Write your code below this line 👇
import math
def paint_calc(height,width,coverage):
    cover=math.ceil((height*width)/5)
    print(f"You'll need {cover} cans of paint.")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
paint_calc(test_h,test_w,5)


