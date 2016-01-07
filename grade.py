from robobrowser import RoboBrowser
from EmailSender import email
import time
from datetime import datetime

calc = 1  # 0 represents grade was not up, 1 is the grade was up
logic = 1
controls = 0
signal = 0
machines = 1
process = 0
nvc = 1
element = 0
dynam = 1
mater = 1
sensor = 0
design = 0

haveSent = [0,0,0,calc,logic,controls,signal,machines,process,nvc,element,dynam,mater,sensor,design,0,0,0] # array grades that were released prior to the check

while True:
    browser = RoboBrowser()
    browser.open('https://student.uwo.ca/psp/heprdweb/?cmd=login')  # western log in website

    formcount=0
    form = browser.get_form(id="login")

    form['userid'].value = 'MYWESTERNID'  # insert western ID
    form['pwd'].value = 'MYWESTERNPASSWORD'  # insert western password

    browser.submit_form(form)  # submits form

    browser.open('https://student.uwo.ca/psc/heprdweb/EMPLOYEE/HRMS/c/UWO_RECORDS_UP.WSA_ES_GRADE_LIST.GBL?Page=WSA_SSR_GRADES&Action=L&ExactKeys=Y&EMPLID=250767551&TargetFrameName=None')

    # ^ transverses to the grade table ^

    bs = browser.parsed

    table = bs.find( "table", id="ACE_DERIVED_AA2_SA_LABEL" )

    rows=list()
    for row in table.findAll("tr"):
       rows.append(row)

    for x in range(3, 13):  # examines each row of the table
        cols = rows[x].find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols[4] != "" and haveSent[x] != 1:  # if a new grade has shown up
            email(cols[0] + ' ' + cols[1])  # sends email for the course found in the row
            haveSent[x] = 1  # sets the course to have sent

    print str(datetime.now())  # gives progress report every 2 and a half minutes
    print haveSent
    print ''

    time.sleep(150)  # sleeps for 2 and a half minutes