username='Tejas01'
password='Tejas@123'
attempt=0
while attempt<3:
        x=input("Enter a name")
        a=input("Enter Username:")
        b=input("Enter password:")
        if a==username and b==password.lower():
                print("Your login Successfully")
                break
        else:
                attempt+=1
                print("Incorrect password Please try again")
                passwords=password
                if attempt==3:
                        passwords=input("Forgot your password.(y/n)")
                        if passwords=='y':
                                passwords=input("Enter your Email id")
                                import random
                                import smtplib
                                otp=random.randint(0,10000)
                                msg = f"Dear {x} Your otp is" + str(otp)
                                server = smtplib.SMTP('smtp.gmail.com', 587)
                                server.starttls()
                                server.login("tejasshah614@gmail.com", "ejshpgqgorgxalto")
                                server.sendmail(passwords, passwords, msg)
                                a = int(input("Enter a otp"))
                                if a==(otp):
                                        print("Verified Successfully")
                                        a=input("Enter new Password")
                                        print("Your Password Successfully Changed")
                                else:
                                        print("Incorrect Otp")
                                server.quit()
                        if passwords=='n':
                                print("Ok Thank you")
