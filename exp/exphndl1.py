
try:
  a=int(input("Enter the num1"))
  b=int(input("Enter the num2"))
  c=a/b
  print(c)
except ZeroDivisionError:
  print("Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
finally: 
 print("Execution ended")