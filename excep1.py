class AgeInvalid(Exception):
	def __init__(self,value):
		self.value = value;

def main():
	try:
		age = int(input("Enter your age : "));
		if(age<18):
			raise(AgeInvalid("Age is Invalid"));

	except AgeInvalid as error:
		print("A new exception occure ",error.value);
		
if __name__ == "__main__":
	main();
