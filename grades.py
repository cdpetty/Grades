import requests as r

def get():
    s = r.Session()
    auth = {'txtUserName':'pettyboys', 'txtPassword':'passWord3'}
    s.post('https://gradespeed.austinisd.org/pc/Default.aspx', data=auth)
    data = {'__EVENTTARGET':'_ctl0$ddlStudents', '__EVENTARGUMENT':'', '_ctl0:ddlStudents':1806207, 'txtUserName':'pettyboys', 'txtPassword':'passWord3', '_ctl0_ddlStudents':1806207, '__EVENTVALIDATION':'/wEWBQLXsfb4BgLdgY3LBwKZtuHrDQLd5cyhDAKIo6qFCyeYwoDIopr3cxP7253q2/MaefDa'}
##    request = s.post('https://gradespeed.austinisd.org/pc/ParentStudentGrades.aspx', data=data)
##    print request.text
    p = s.get('https://gradespeed.austinisd.org/pc/ParentStudentGrades.aspx:57', data=data)
    print p.text
if __name__=='__main__':
    get()
    
    
##form = document.getElementById('aspnetForm')
##form.__EVENTTARGET.value ='_ctl0$ddlStudents'
##form.__EVENTARGUMENT.value = ''
##otherForm = document.getElementById('_ctl0_ddlStudents')
##otherForm.value = '1806207'