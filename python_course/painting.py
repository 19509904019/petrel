'''
Author: yujun
Date: 2022-03-07 22:44:30
LastEditors: yujun
LastEditTime: 2022-03-07 22:44:30
FilePath: \project\painting.py
Description: 

'''
#绘制奥运五环


import turtle

turtle.width(8)  #加粗


#上排第一个圈
turtle.color("blue")
turtle.circle(40)
turtle.penup()
turtle.goto(100,0)
turtle.pendown()


#上排第二个圈
turtle.color("black")
turtle.circle(40)
turtle.penup()
turtle.goto(200,0)
turtle.pendown()


#上排第三个圈
turtle.color("red")
turtle.circle(40)
turtle.penup()
turtle.goto(50,-30)
turtle.pendown()

#下排第一个圈
turtle.color("yellow")
turtle.circle(40)
turtle.penup()
turtle.goto(150,-30)
turtle.pendown()

#下排第二个个圈
turtle.color("green")
turtle.circle(40)


turtle.done()


