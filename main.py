import turtle

poly = turtle.Turtle()
poly.degrees(360.0)
poly.speed("slowest")
poly.penup()
poly.goto(-150, 300)
poly.pendown()
poly.speed("fastest")

sides = int(input("Enter number of sides: "))
inner_angle = 180 - (((sides - 2) * 180) / sides)
move = 1500 / sides

for i in range(sides):
    print("SIDE", i+1)
    poly.forward(move)
    poly.right(inner_angle)

input("")