import random
x=True
while(x):
    print("Do you want to play Number Guessing Game?")
    print("Enter Y for Yes")
    print("N for No")
    ch=input()
    ch=ch.lower()
    if ch=="y":
        x=random.randint(1,100)
        g=int(input("Guess the number from 1 to 100:"))
        count=0
        while x!=g:
            if x>g:
                print("Your number is to low")
                g=int(input("Guess the number"))
                count+=1
            elif x<g:
                print("your number is to high")
                g=int(input("Guess the number"))
                count+=1
        else:
            count+=1
            print(f"you guessed the correct number in {count} attempts")
            
    elif ch=="n":
        x=False
        print("Game Exit")
    else:
        print("Enter the correct input")
    
        
