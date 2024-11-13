try:
    num=int(input("enter any integer value:--"))
    print(num)
except ValueError as ex:
    print("exception:", ex)

print("i am outside the try block")    
