import math
def line_length(dot1, dot2):
	distX = dot1[0] - dot2[0]
	distY = dot1[1] - dot2[1]
	return round(math.sqrt((distX ** 2 + distY ** 2)),2)