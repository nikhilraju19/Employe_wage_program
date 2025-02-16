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
            return full_day_hr, daily_wage
        case "part_time":
            daily_wage = wage_per_hr*part_time_hr
            return part_time_hr, daily_wage
        case "absent":
            daily_wage = 0
            return 0, daily_wage

def monthly_wage():
    """
	Description:
		This function is used to calculate the monthly wage of an employee based on part time and full time attendance
	Parameters:
		None
	Return:
		The monthly wage of the employee
    """  
    total_monthly_wage = 0
    total_working_hr = 0
    total_working_days = 0
    
    # Calculate Wages till a condition of total working hours or days is reached for a month 
    # Assume 100 hours and 20 days
    while total_working_hr < 100 and total_working_days <20:
        each_day_working_hr, daily_wage = cal_emp_daily_wage()
        total_working_days += 1
        total_working_hr += each_day_working_hr
        total_monthly_wage += daily_wage
    
    print(f"Monthly wage till a condition of total working hours or days reached is: {total_monthly_wage}")
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