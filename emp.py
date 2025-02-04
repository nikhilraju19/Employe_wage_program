import random

def chk_attd():
	attendance = random.choice([0,1])
	return attendance

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
			print(f"The employee is present and worked full time, his daily wage is: {daily_wage}")
		case "part_time":
			daily_wage = wage_per_hr*part_time_hr
			print(f"The employee is present and worked part time, his daily wage is: {daily_wage}")
		case "absent":
			daily_wage = 0
			print(f"The employee is absent and his daily wage is: {daily_wage}")
		

if __name__ == "__main__":
	cal_emp_daily_wage()
