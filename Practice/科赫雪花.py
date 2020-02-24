import turtle as t

def koch(size,n):
        if n == 0:
                t.fd(size)
        else:
                for angle in [0,60,-120,60]:
                        t.left(angle)
                        koch(size/3,n-1)
                        
def main(size,n):
        t.setup(800,800)
        t.penup()
        t.goto(-300,200)
        t.pendown()
        t.pensize(2)
        t.pencolor("pink")
        for i in range(3):
                koch(size,n)
                t.right(120)
        
main(500,3)
