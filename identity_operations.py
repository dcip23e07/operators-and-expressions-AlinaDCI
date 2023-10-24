var_a = 400
var_b = '200' + '200'
var_c = 400.0
var_d = 200 + 200

# 1. What is the result of :
print ("Result var_a == var_b:", var_a == var_b ) # False: failed attempt to compare int and str
print ("Result var_a is var_b:", var_a is var_b) # False: in arithmetical sense it is true, but these two values are not the same object

# 2. What is the result of :
print ("Result var_a == var_c:", var_a == var_c) # True: both variables = 400 (same value)
print ( "Result var_a is var_c: ", var_a is var_c) # False: 400 and 400.0 would be different objects

# 3. What is the result of :
print ("Result var_a == var_d:", var_a == var_d) # True: the variables have the same value 400
print ("Result var_a is var_d:", var_a is var_d) # True: they refer to the same object