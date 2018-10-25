#sending a mail
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("aishpreetham@gmail.com","lalithavenkatesh")

msg="hello"
server.sendmail("aishpreetham@gmail.com","varshapn27@gmail.com",msg)
print('Mail is sent...')
server.quit() 