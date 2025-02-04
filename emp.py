import random

def chk_attd():
	attendance = random.choice([0,1])
	return attendance

def cal_emp_daily_wage():
	emp_check = chk_attd()
	wage_per_hr = 20
	full_day_hr = 8
	if emp_check == 1:
		daily_wage = wage_per_hr * full_day_hr
		print(f"The employee is present and worked full time, his daily wage is: {daily_wage}")
	else:
		daily_wage = 0
		print(f"The employee is absent and his daily wage is: {daily_wage}")

if __name__ == " __main__ ":
	cal_emp_daily_wage()
