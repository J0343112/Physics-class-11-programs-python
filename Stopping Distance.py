import os 
import time

print("Condition: is the object  in constant acceleration y/n?")
choice=input("type here :")
rc=choice[0]
def main():
    os.system("cls")

    u=float(input("the initial velocity (in SI):"))
    a=float(input("the acceleration (in SI) :"))
    
    s1=u*u/2*a

    print("the stopping distance is :{:.2f}m".format(s1))

if rc=="y":
    print ("proceed...")
    time.sleep(2)
    main()
else:
    print("sorry cant help :-(")    
    exit()