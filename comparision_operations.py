var_a = 1500 + 3000
var_b = 1500 + 3000.00
var_c = "4500"
var_d = 4500.000001
var_e = 1000
var_f = 5000 - 500
var_g = 60000

# 1. Print out the following values in your script
print (var_a == var_b) # True 
print (var_a >= var_b) # True
print (var_a > var_b) # False
print (var_a > var_c) # Failed: int and str cannot be compared 
print (var_a > var_d) # False
print (var_g < var_b) # False
print (var_a != var_c) # True
print (var_e == var_f) # False