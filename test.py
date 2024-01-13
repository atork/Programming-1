import time


def repitition(number):
    string = str(number)
    num = int(string[0])
    x=1
    while x < number:
        string=string+string[0]
        x+=1
    
    print(string)
    time.sleep(1)
    repitition(num+1)

repitition(1)