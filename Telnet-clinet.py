import telnetlib
import smtplib

# HOST = "smtp.gmail.com"
# tb = telnetlib.Telnet(HOST, "587")
# print (tb.read_all())

gmail_user = 'afshinshah77@gmail.com'
gmail_password = 'invincible98@'
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print("something went wrong\n")
