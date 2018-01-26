#Katie Chiu
#Computer Programming 12th
#January 11, 2018

def lists():
    names=["Emma", "Ava", "Jayden", "Daniel", "Ella"]
    numbers=[13, 83, 54, 72, 93]
    both=[names+numbers]
    print(names, numbers, both)
    names[4:4]=["Nathan"]
    names[2:2]=["Amelia"]
    print(names)
lists()
