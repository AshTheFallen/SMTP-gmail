import telnetlib
import smtplib

# HOST = "smtp.gmail.com"
# tb = telnetlib.Telnet(HOST, "587")
# print (tb.read_all())

gmail_user = 'afshinshah77@gmail.com'
gmail_password = 'invincible98@'

sent_from = gmail_user
to = ['ali.goldani97@gmail.com']
subject = 'smtp-test1'
body = 'hi Ali'

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
