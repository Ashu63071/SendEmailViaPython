import smtplib

#content is the information to be sent
content = 'Hello! this is email using Python'
mail = smtplib.SMTP('smpt.gmail.com',587)

mail.ehlo()
mail.starttls()

#person who is sending email and its password
hostmail = 'abcde@gmail.com'
password = 'PASSWORD'

#person to whom the mail should be sent
guestmail='xyz@gmail.com'

#login email ID and Password of the sender
mail.login(hostmail,password)

mail.sendmail(hostmail, guestmail ,content)

mail.close()
