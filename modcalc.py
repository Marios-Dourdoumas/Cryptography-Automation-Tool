#modcalc 1.2
#Dourdoumas Marios
#Ergaleio gia epalhtehysh ypologismwn, eyresh taskewn, prwtwn arithmwn kai antistrofwn
#<---allages--->
#1.2 -> ypologismos DHP
import math 

            #Synarthseis 
#<--------------------------------------->
def modcalcu(x,y,z):
    print("The result is: ")
    print(pow(x,y,z))

def ordercalc(x,z):
    y = 1
    while (pow(x,y,z) != 1):
        y = y+1
        
    print("Order is: ",y)
    
def primes(x):
    pf=[]
    for i in range(2,x):
        if(x%i == 0):
            pf.append(i)
    print("Prime Factors are: ",pf)
            
def euclid(a,b):
    t = b
    mods = []
    quotients = []
    x = [0,1]
    i = 0 
   
    while (b%a != 0):
        q = b//a
        r = b % a
        b = a * q + r
        mods.append(b%a)
        quotients.append(b//a)
        b = a
        a = r
        
    for i in range(2,len(quotients)+2):
        new = ( x[i-2] - (x[i-1] * quotients[i-2]) ) % t
        x.append(new)
        
    print("Reverse is: ",x[-1])
    
def diffie(x):
    a = int(input("Base: "))
    p = int(input("Prime: "))
    res = 0
    for i in range (1,p):
        res = pow(a,i,p)
        if(res == x):
            return i
    

def menu():
    x = input("[1]: Calculate Modulo \n[2]: Calculate Order\n[3]: Calculate Prime Factors\n[4]: Find inverse of modulo\n[5]: Calculate DHP\nEnter Option: ")

    if(x == "1"):
        x = int(input("Enter Base: "))
        y = int(input("Enter Exponent: "))
        z = int(input("Enter Modulo: "))
        modcalcu(x,y,z)
    elif(x == "2"):
        x = int(input("Enter Base: "))
        z = int(input("Enter Modulo: "))
        ordercalc(x,z)
    elif(x == "3"):
        x = int(input("Enter a number: "))
        primes(x)
    elif(x == "4"):
        a = int(input("Enter Base: "))
        b = int(input("Enter Modulo: "))
        euclid(a,b)
    elif(x == "5"):
        x = int(input("Known element: "))
        res = diffie(x)
        print("The answer is: {}".format(res))
    
#<---------------------------------------------------->
#main program
c = 'y'
while(c == 'y'):
    menu()

    c = input("Do you want to calculate again? [y/n] ")
