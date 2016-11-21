# python3
import smtplib
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
email_conn.login(username, password)

email_conn.sendmail(from_email, to_list, "This is a test email from python")
email_conn.quit()
