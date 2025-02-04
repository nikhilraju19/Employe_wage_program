import random

def chk_attd():
	attendance = random.choice([0,1])
	return attendance

def monthly_wage():
    total_monthly_wage = 0
    for i in range(20):
        total_monthly_wage += cal_emp_daily_wage()
    print(f"Monthly wage of an employee is: {total_monthly_wage}")
        

def cal_emp_daily_wage():
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
			return daily_wage
		case "part_time":
			daily_wage = wage_per_hr*part_time_hr
			return daily_wage
		case "absent":
			daily_wage = 0
			return daily_wage
		

if __name__ == "__main__":
	monthly_wage()
