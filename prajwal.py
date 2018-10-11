import smtplib

# Creates SMTP Session
s=smtplib.SMTP('smtp.gmail.com',587)

# start TLS for security
s.starttls()

# Authentication
s.login("prajwal432001@gmail.com","Prajwal@12345")

# Message to be sent
message="GOOD MORNING BRO"

#sending the mail
s.sendmail("prajwal432001@gmail.com","prajwal432001@gmail.com",message)           
print("success")                             

# terminating the session
s.quit()