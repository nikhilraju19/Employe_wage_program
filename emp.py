import random


def chk_attd():
	"""
		Description:
			This function is used to check the attendance of an employee
		Parameters:
			None
		Return:
			bool: True if the employee is present, False otherwise.
 	"""
	# Generate a random attendance status (1 for present, 0 for absent)
	attendance = random.choice([0,1])
	if attendance == 1:
		print("The employee is present")
		return True
	else:
		print("The employee is absent")	
		return False
  
def main():
    """
		Description:
			This function calls all necessary sub-functions to perform the intended operations 
   			of the program. It serves as the entry point when the script is run.
		Parameters:
			None
		Return:
			None
    """
    print("Welcome to employee wage computation.")
    chk_attd()

if __name__ == "__main__":
	main()
	
 