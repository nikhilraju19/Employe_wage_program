import random

def chk_attd():
	attendance = random.choice([0,1])
	return attendance

def cal_emp_daily_wage():
	emp_check = chk_attd()
	wage_per_hr = 20
	full_day_hr = 8
	part_time_hr = 4
	if emp_check == 1 and random.random()>=0.5:
		daily_wage = wage_per_hr * full_day_hr
		print(f"The employee is present and worked full time, his daily wage is: {daily_wage}")
	elif emp_check == 1 and random.random()<0.5:
		daily_wage = wage_per_hr * part_time_hr
		print(f"The employee is present and worked part time, his daily wage is: {daily_wage}")
	else:
		daily_wage = 0
		print(f"The employee is absent and his daily wage is: {daily_wage}")

if __name__ == "__main__":
	cal_emp_daily_wage()
