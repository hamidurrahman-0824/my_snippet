def age_format(dob:tuple,crd:tuple)->tuple:
	dy,dm,dd= dob
	cy,cm,cd= crd
	years = cy-dy
	months = cm-dm
	if (cm,cd)<(dm,dd):
		years -=1
		months = (cm-dm)%12
	if cd<dd:
		months-=1
		days = (cd+31)-dd
	else:
		days = cd -dd
	return (years,months,days)
print(age_format((2003,3,26),(2026,2,16)))
exit()
def age_in_yymmdd(dob:tuple,cda:tuple)->str:
	dy,dm,dd= dob
	cy,cm,cd= cda
	years = cy-dy
	months = (cm-dm)
	days = cd-dd
	if (cm,cd)<(dm,dd):
		years-=1
		months= (cm-dm)%12
	if cd<dd:
		months-=1
		days = (cd+31)-dd
	else:
		days = cd-dd
	return years,months,days
	print(years,months,days)
	#				  2002/01/26
	#				  2026/02/15
	
print(age_in_yymmdd((2003,3,26),(2026,2,16)))
print(-1%12)
exit()
def divisible_by_100(x:int)->bool:
	return bool(x%100==0)

def divisible_by_400(x:int)->bool:
	return bool(x%400==0)
	
def leap_year(year:int)->bool:
	if divisible_by_400(year):
		return True
	if divisible_by_100(year):
		return False
	return year%4==0#same as bool(year%4==0)
def is_leap_year(year:int)-> bool:
	if year%400==0 and year%100==0:
		return True
	return year%4==0
if __name__=='__main__':
	assert leap_year(2004)==True
	assert leap_year(1900)==False
	assert leap_year(2000)==True
	assert leap_year(2011)==False
	print('passed')
def age_in_ymd(birth_y, birth_m, birth_d, today_y, today_m, today_d):
    years = today_y - birth_y
    months = today_m - birth_m
    days = today_d - birth_d

    # Adjust if birthday hasn't happened yet this year
    if (today_m, today_d) < (birth_m, birth_d):
        years -= 1
        months = (today_m - birth_m) % 12

    # Adjust days manually
    if today_d < birth_d:
        months -= 1
        # Approximate: assume previous month had 31 days
        days = (today_d + 31) - birth_d
    else:
        days = today_d - birth_d

    return years, months, days

print(age_in_ymd(2003, 3, 26, 2026, 2, 15))

from datetime import date

birthdate = date(2003, 3, 26)
today = date(2026, 2, 15)

# Calculate difference
years = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    years -= 1

months = (today.month - birthdate.month) % 12
days = (today - date(today.year, birthdate.month, birthdate.day)).days if today.day >= birthdate.day else (today - date(today.year, birthdate.month-1, birthdate.day)).days

print(f"{years} years, {months} months, {days} days")

