import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'saumytiwari009@gmail.com'
email_passwd = 'bedw rxqm pdkw iawv'

#mtd.nithin@gmail.com
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='saumytiwari7@gmail.com', msg="Hi Nithin,\n \nOur team is Team 1 (T1) and the participants are : \n\n 1. Saumy Tiwari  \n 2. Francis Xavier K \n \n The case study we are working is : 2 (MCQ Based Online Exam Application)\n\nAnd my GitHub repository link is :\n https://github.com/saum13/python_trainings_sep2024 \n \n  \n Thanks and Regards, \n Saumy Tiwari")
connection.close()
print('Mail sent successfully')