try:
    age=int(input("enter you age:--"))
    if age%2==0:
               print("your age is a even number")
    else:
        print("your age is a ood number")
except ZeroDivisionError:
      print("0 age is not valid") 
except ValueError:
    print("enter only integer value")
except NameError as ex:
    print("the exception is ",ex)
except:
    print("some error accoured") 
finally:
    print("i wll execute no matter what") 