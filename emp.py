import random


def chk_attd():
    """
	Description:
		This function is used to check the attendance of an employee
	Parameters:
		None
	Return:
		attendance
    """
    attendance = random.choice([0,1])
    return attendance

def cal_emp_daily_wage():
    """
	Description:
		This function is used to calculate the daily wage of an employee based on part time and full time
	Parameters:
		None
	Return:
		The daily wage of the employee
    """
    emp_check = chk_attd()
    if emp_check == 1:
        work_type = random.choice(["full_time", "part_time"])
    else:
        work_type = "absent"
    wage_per_hr = 20
    full_day_hr = 8
    part_time_hr = 4
    match work_type:
        case "full_time":
            daily_wage = wage_per_hr*full_day_hr
            print(f"The employee is present and worked full time, his daily wage is: {daily_wage}")
            return daily_wage
        case "part_time":
            daily_wage = wage_per_hr*part_time_hr
            print(f"The employee is present and worked part time, his daily wage is: {daily_wage}")
            return daily_wage
        case "absent":
            daily_wage = 0
            print(f"The employee is absent and his daily wage is: {daily_wage}")
            return daily_wage
  
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
    cal_emp_daily_wage()

if __name__ == "__main__":
	main()
