from smtplib import SMTP

def email(course):
    sender = 'sender@email.com'  # put your email here
    receivers = ['receiver1@email.com', 'receiver2@email.com']  # put receiver emails here

    header = 'To:'  # leave blank for receivers to be anonymous

    header = header + '\n' + 'From: ' + sender + '\n' + 'Subject: ' + course + ' \n'
    print header  # outputs what has been sent
    msg = header + '\n Grade has been released \n\n'


    smtpObj = SMTP('smtp.broadband.rogers.com', 587)  # set up for @rogers.com email addresses
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('youremail@rogers.com', 'yourpassword') # put your login credentials for your email account
    smtpObj.sendmail(sender, receivers, msg)
    print "Successfully sent email \n"  # prints if everything has been successfully done
    smtpObj.close()