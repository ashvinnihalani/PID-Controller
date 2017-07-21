import math
def res_to_temp(res){
	C = 1-res/1000 #Constant Term, change the divisor if refrence resistance is not 1000
	A =  3.9083E-3  #Platnum constant the linear terms
	B = -5.775E-7 #The quardractic term
	return -a+math.sqrt(a**2-4*b*c))/2*b
}
