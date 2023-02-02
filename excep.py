print("--------Exception handling---------- ");

no1 = int(input("Enter first number : "));
no2 = int(input("Enter second number : "));

try:
	ans = no1/no2;
	print("Division is : ",ans);

except:
	print("Unable to divide by zero ");

finally:
	print("Inside finally block to realese all resources ");

print("End of exception handling application ");
