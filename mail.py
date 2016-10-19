from flask import request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#respone code change via email status.
respone = 200
#email sending function need strings of the form values so it is changable.
def send(NAME, FROM, SUBJECT, MESSAGE):
	From = request.form[FROM]
	To = 'gil5841@gmail.com'
	Subject = request.form[SUBJECT]
	msg = MIMEMultipart()
	msg['Subject'] = Subject
	msg['From'] = From
	msg['To'] = To
	mess = """Hey Gil, \r\n \r\n %s send you a message about: \r\n \r\n %s \r\n \r\n the message says:  \r\n \r\n %s \r\n \r\n if you want to responde this is the email:      %s""" % (request.form[NAME], Subject, request.form[MESSAGE], From)

	text = MIMEText(mess, 'plain')
	msg.attach(text)
	try:
		mail = smtplib.SMTP('mail.smtp2go.com', 8025)
		mail.ehlo()
		mail.starttls()
		mail.ehlo()
		mail.login('GoldzweigApps@info.com', 'Gil5841!')
		mail.sendmail(From, To.split(','), msg.as_string())   
		mail.close()      
		respone = 200
		return 'Mail send seccessfully'
	except Exception as e:
		respone = 400
		return 'error: %s' %(e.message)


def sendTo(NAME, FROM, TO, SUBJECT, MESSAGE):
	From = request.form[FROM]
	To = request.form[TO]
	Subject = request.form[SUBJECT]
	msg = MIMEMultipart()
	msg['Subject'] = Subject
	msg['From'] = From
	msg['To'] = To
	mess = """Hey Gil, \r\n \r\n %s send you a message about: \r\n \r\n %s \r\n \r\n the message says:  \r\n \r\n %s \r\n \r\n if you want to responde this is the email:      %s""" % (request.form[NAME], Subject, request.form[MESSAGE], From)

	text = MIMEText(mess, 'plain')
	msg.attach(text)
	try:
		mail = smtplib.SMTP('mail.smtp2go.com', 8025)
		mail.ehlo()
		mail.starttls()
		mail.ehlo()
		mail.login('GoldzweigApps@info.com', 'Gil5841!')
		mail.sendmail(From, To.split(','), msg.as_string())   
		mail.close()      
		respone = 200
		return 'Mail send seccessfully'
	except Exception as e:
		respone = 400
		return 'error: %s' %(e.message)		
#getting the respone code to return the currect status		
def get_respone():
		return respone	

