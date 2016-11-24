# python3
# smtp mail lib
import smtplib
# html format lib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# sending email using gmail
host = "smtp.gmail.com"
port = 587
username = "your google account"
password = "your password"
# showing who send this email
from_email = username
to_list = ["your target"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()

msg = MIMEMultipart("alternative")
msg['Subject'] = "The Subject"
msg['From'] = from_email
# msg['To'] = to_list

plain_txt = "This is plain text"
html_txt = """\
<html>
    <head></head>
    <body>
        <h1>Test HTML</h1>
        <p>Testing <b>HTML</b> content by <a href="https://www.facebook.com/yenhao0218" target="blank">Eric</a></p>
    </body>
</html>
"""

part_1 = MIMEText(plain_txt, 'pain')
part_2 = MIMEText(html_txt, 'html')

msg.attach(part_1)
msg.attach(part_2)

try:
    email_conn.login(username, password)
    email_conn.sendmail(from_email, to_list, msg.as_string())
except smtplib.STMPAuthenticationError:
    print("Could not login")
except smtplib.SMTPException:
    print("Error occured sending email")

email_conn.quit()
