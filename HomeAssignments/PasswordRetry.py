password = "openAI123" 
attempts = 3
userinput = input("Enter your password: ")

for i in range(attempts):
    if userinput==password:
        print("Login Successful")
        break
    else:
        attempts = attempts - 1
        if attempts == 0:
            print("Account Locked")
        else:
            print("Incorrect Password. You have", attempts, "attempts left.")
            userinput = input("Re-enter your password: ")
            