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
    # Use match to calculate the daily wage based on specific work type
    match work_type:
        case "full_time":
            daily_wage = wage_per_hr*full_day_hr
            return daily_wage
        case "part_time":
            daily_wage = wage_per_hr*part_time_hr
            return daily_wage
        case "absent":
            daily_wage = 0
            return daily_wage

def monthly_wage():
    """
	Description:
		This function is used to calculate the monthly wage of an employee based on part time and full time attendance
	Parameters:
		None
	Return:
		The daily wage of the employee
    """  
    total_monthly_wage = 0
    # Assume 20 Working Day per Month
    for i in range(20):
        total_monthly_wage += cal_emp_daily_wage()
    print(f"Monthly wage of an employee is: {total_monthly_wage}")
    return total_monthly_wage
  
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
    monthly_wage()

if __name__ == "__main__":
	main()
 