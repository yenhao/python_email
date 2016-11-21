# python_email

Remember to turn on the setting in gmail

1. turn on the pop
2. turn on the IMAP

If you get `534` error while try to login using python

Go to Google's Account Security Settings: www.google.com/settings/security

Find the field "Access for less secure apps". Set it to "Allowed".

Try your script again, changing server.sendemail() to server.sendmail()
