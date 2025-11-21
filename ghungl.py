password = "67no41no61"
attempt = ""
tries = 0 
while attempt != password and tries <3:
    attempt = input("Enter password")
    tries+= 1 
    
    if attempt != password:
        print("!ncorrect password! Try again.")
        
if attempt == password:
    print("Access granted!")
else:
    print("Too many attempts. Try later")


list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]