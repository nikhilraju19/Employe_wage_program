import random

def chk_attd():
	attendance = random.choice([0,1])
	return attendance

def monthly_wage():
    total_monthly_wage = 0
    total_working_hr = 0
    total_working_days = 0
    
    while total_working_hr < 100 and total_working_days <20:
        each_day_working_hr, daily_wage = cal_emp_daily_wage()
        total_working_days += 1
        total_working_hr += each_day_working_hr
        total_monthly_wage += daily_wage
    
    print(f"Monthly wage till a condition of total working hours or days reached is: {total_monthly_wage}")
         
        
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
			return full_day_hr, daily_wage
		case "part_time":
			daily_wage = wage_per_hr*part_time_hr
			return part_time_hr, daily_wage
		case "absent":
			daily_wage = 0
			return 0, daily_wage

if __name__ == "__main__":
    monthly_wage()
