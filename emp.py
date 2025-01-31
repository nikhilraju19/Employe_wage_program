import random

def chk_attd():
	print("Welcome to employee wage computation program on Main branch")
	attendance = random.choice([0,1])
	if attendance == 1:
		print("The employee is present")
	else:
		print("The employee is absent")	

if __name__ == "__main__":
	chk_attd()
	print("Welcome to employee wage computation")
