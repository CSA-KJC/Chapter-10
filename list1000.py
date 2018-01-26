#Katie Chiu
#Computer Programming 12th
#January 24, 2018

x=["Amber", "Blake", "Anna", "Dave", "River"]
   
def lists(y):
    print(y)
    ask=input("Enter a name to add to the list: ")
    y.append(ask)
    print(y)
    return y

def newname(old):
    ask2=input("Do you want to add another name? ").upper()
    if ask2=="YES":
        name=input("Enter a name to add to the list: ")
        old.append(name)
        print(old)
        newname(old)
    elif ask2=="NO":
        print("Here is the final list: "+str(old))
    else:
        print("That is not a valid answer. Try again")
        newname(old)
        
lists(x)
newname(x)
