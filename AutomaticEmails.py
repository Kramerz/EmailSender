import smtplib
import tkinter


emailGui = tkinter.Tk()



def messageDeilver():

	conn = smtplib.SMTP("smtp.gmail.com", 587)
	sender = 'UserPrincipalName'	
	receivers = ['UPN']
	message = """From: Ryan West <UPN>
To: Ryan <UPN>
Subject: SMTP E-mail test
This is a test e-mail message.
"""
	conn = smtplib.SMTP('smtp.gmail.com', 587)
	conn.ehlo()
	conn.starttls()
	conn.login('UserPrincipalName', 'Password')
	conn.sendmail(sender, receivers, message)
	conn.quit()
	

Label = Label(emailGui, text = "Send Email")

emailGui.geometry('450x450+500+300')
emailGui.title("Super cool Email System")
sendEmail = tkinter.Button(emailGui, text="Send Email!", command = messageDeilver)

sendEmail.pack()
Label.pack()






emailGui.mainloop()
