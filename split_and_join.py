#Katie Chiu
#Computer Programming 12th
#January 25, 2018

def split():
    string="My name is Jose"
    cut=string.split()
    print(cut)

def user():
    string="user1;user2;user3"
    cut=string.split(';')
    print(cut)

def add():
    lists=["this","is","a","sentence"]
    print(" ".join(lists))
    
split()
user()
add()
