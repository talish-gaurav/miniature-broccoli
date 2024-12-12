try:
   num1 , num2 = eval(input("Enter your two numbers seperated by  a comma "))
   result = num1/num2
   print("The result is:",result)

except ZeroDivisionError:
   print("Number can not be divided by zero")
except ValueError:
   print("You have not entered an integer")
except SyntaxError:
   print("There is no comma in place")
except:
   print("There is an exception")
else:
   print("No error")
finally:
   print("Command finished")