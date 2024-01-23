def total_overs(balls):
	b = balls % 6
	overs = int((balls - b) / 6)
	return float(str(overs) + "." + str(b))