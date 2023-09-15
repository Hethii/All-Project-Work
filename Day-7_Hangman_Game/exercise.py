# Explaining NOT
# as long as y is not true in the code, it will keep on running. 
# anytime Y changes to true, it stops running 
y = False
z = 0
while not y:
    z += 1
    print(z)
    y = True 
    if z == 10:
        y = True
    print("end")
    
