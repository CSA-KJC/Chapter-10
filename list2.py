#Katie Chiu
#Computer Programming 12th
#January 17, 2018

def lists():
    x=[29, "April", 2003, "Houston"]
    for y in x:
        print(y)
    print("I was born in "+x[3])
    print("The month was "+x[1])
    x[3:3]=["Michael"]
    print(x)

lists()
