while(1):
    x=input()
    if(x=="Quit"):
    #close the program
        break
    elif(int(x)==0):
        print("ZERO")
    elif(int(x)<0):
        print("NEGATIVE")
    elif(int(x)>0):
        print("POSITIVE")
print("Done")