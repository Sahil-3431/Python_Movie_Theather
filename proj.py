import random
total1=0
total2=0
total3=0
while True:
    print("1.movies")
    print("2.snacks")
    print("3.coldrink")
    print("4.exit")
    y=int(input("enter your choice"))
    if(y==1):
        while True:
            print("1.KGF2")
            print("2.SALAAR")
            print("3.ANIMAL")
            print("4.EXIT")
            c=int(input("enter your choice"))
            if(c==1):   
                while True:
                    print("you are choose KGF2 movie")
                    print("tickets price..")
                    print("1.royal->300rs")
                    print("2.club->200rs")
                    print("3.exicutive->150rs")
                    print("4.exit")
                    x=int(input("enter your ticket choice"))
                    if(x==1):
                        q=int(input("how many tickets"))
                        total1=total1+q*300
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==2):
                        q=int(input("how many tickets"))
                        total1=total1+q*200
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==3):
                        q=int(input("how many tickets"))
                        total1=total1+q*150
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==4):
                        break
            elif(c==2):
                while True:
                    print("you are choose SALAAR movie")
                    print("tickets price..")
                    print("1.royal->350rs")
                    print("2.club->250rs")
                    print("3.exicutive->180rs")
                    print("4.exit")
                    x=int(input("enter your ticket choice"))
                    if(x==1):
                        q=int(input("how many tickets"))
                        total1=total1+q*350
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==2):
                        q=int(input("how many tickets"))
                        total1=total1+q*250
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==3):
                        q=int(input("how many tickets"))
                        total1=total1+q*180
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==4):
                        break    
            elif(c==3):
                while True:
                    print("you are choose ANIMAL movie")
                    print("tickets price..")
                    print("1.royal->300rs")
                    print("2.club->200rs")
                    print("3.exicutive->150rs")
                    print("4.exit")
                    x=int(input("enter your ticket choice"))
                    if(x==1):
                        q=int(input("how many tickets"))
                        total1=total1+q*300
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==2):
                        q=int(input("how many tickets"))
                        total1=total1+q*200
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==3):
                        q=int(input("how many tickets"))
                        total1=total1+q*150
                        print("your tickets number are")
                        for i in range(1,q+1):
                            s=random.randint(100,1000)
                            print(s)
                    elif(x==4):
                        break
            elif(c==4):
                print("total tickets amount is---->",total1)
                break
    elif(y==2):
        while True:
            print("1.popcorn")
            print("2.pizza")
            print("3.bread")
            print("4.exit")
            c=int(input("enter the choice"))
            if(c==1):
                 while True:
                    print("1.salted popcorn 180g-->300rs")
                    print("2.caramel popcorn 180g-->390rs")
                    print("3.cheese popcorn 180g-->420rs")
                    print("4.exit")
                    d=int(input("which one do you want"))
                    if(d==1):
                        total2=total2+300
                    elif(d==2):
                        total2=total2+390
                    elif(d==3):
                        total2=total2+420
                    elif(d==4):
                        break
            elif(c==2):
                while True:
                    print("1.Maxican pizza-->359rs")
                    print("2.panner pizza-->300rs")
                    print("3.exit")
                    d=int(input("which one do you want"))
                    if(d==1):
                        total2=total2+359
                    elif(d==2):
                        total2=total2+300
                    elif(d==3):
                        break
            elif(c==3):
                while True:
                    print("1.vegitable burger-->239rs")
                    print("2.panner tikka sandwich-->300rs")
                    print("3.exit")
                    d=int(input("which do you want"))
                    if(d==1):
                        total2=total2+239
                    elif(d==2):
                        total2=total2+300
                    elif(d==3):
                        break
            elif(c==4):
                print("total snacks amount is-->",total2)
                break
    elif(y==3):
        while True:
            print("1.large pepsi-->270rs")
            print("2.regular pepsi-->200rs")
            print("3.small pepsi-->150rs")
            print("4.exit")
            p=int(input("which do you want"))
            if(p==1):
                q=int(input('how many glass'))
                total3=total3+q*270
            elif(p==2):
                q=int(input("how many glass"))
                total3=total3+q*200
            elif(p==3):
                q=int(input("how many glass"))
                total3=total3+q*150
            elif(p==4):
                print("total coldrinks amount is-->",total3)
                break
    elif(y==4):
        print("movie bill-->",total1)
        print("snacks bill-->",total2)
        print("colddrink bill-->",total3)
        B=total1+total2+total3
        print(" ")
        print("YOUR TOTAL BILL IS--->",B)
        print(" ")
        break      




