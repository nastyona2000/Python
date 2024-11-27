#login = input("Enter your email: ")
#password = input("Enter your password: ")
right_login = "user228"
right_password = 15 #з двох цифр

for t in range(10):
    for f in range(10):
        pas = t*10 + f
        print(pas)
        if pas == right_password:
            print("ACCESS GRANTED! Pass: ", pas);
            break
    if pas == right_password:
            print("ACCESS GRANTED! Pass: ", pas);
            break
  
    
