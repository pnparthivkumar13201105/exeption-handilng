try:
    num1=int(input("enter the first integer number:--"))
    num2=int(input("enter the second integer number:--"))
    result=num1/num2
    print("the value =",result)
    print("the value is =",result1)
except ZeroDivisionError:
    print("division by 0 is not allowed")
except ValueError:
    print("enter only integer value")
except NameError as ex:
    print("the exception is ",ex)
except:
    print("some error accoured") 
finally:
    print("i wll execute no matter what")                   