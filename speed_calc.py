def speed_calc(distance:float,time:float)->float:
	if time<=0:
		return "Time must be greater than zero"
	return f"{distance/time:.2f} m/s"
print(speed_calc(160,15))
