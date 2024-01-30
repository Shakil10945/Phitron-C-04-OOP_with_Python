for i in range(1,6):
    for j in range(1,i+1):
        if i==j:
            print(j)
            break
        print(f"{j} ", end='')
