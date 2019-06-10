import telnetlib
import smtplib

# HOST = "smtp.gmail.com"
# tb = telnetlib.Telnet(HOST, "587")
# print (tb.read_all())

gmail_user = 'email address'
gmail_password = 'password'

sent_from = gmail_user
to = ['reciver email']
subject = 'smtp-test1'
body = 'body of email'

email_text = """  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
except:
    print("something went wrong\n")
