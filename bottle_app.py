from bottle import route, post, template, default_app, error
import sqlite3

#set up db connection
companyDb = sqlite3.connect("/home/onurucar/mysite/databases/company.db")
companyCursor = companyDb.cursor()

@route('/')
def Main():
    return template('mainmenu.html')

@route('/employeeMain')
def employeeMainMenu():
    return template('empMain.html')

@route('/employeeView')
def viewContacts():
    return template('view.html', c = companyCursor)

@route('/addEmp')
def addEmp():
    return template('add_emp.html')

@post('/addEmpSuccess')
def addEmpSuccess():
    return template('addEmpSuccess.html', c = companyCursor, db = companyDb)

@route('/editEmp')
def editEmp():
    return template('editEmp.html', c = companyCursor)

@post('/editMenu')
def editMenu():
    return template('editMenu.html', c = companyCursor)

@post('/editSuccess')
def editSuccess():
    return template('editSuccess.html', c = companyCursor, db = companyDb)

@route('/deleteEmp')
def deleteEmp():
    return template('deleteEmp.html', c = companyCursor)

@post('/deleteMenu')
def deleteMenu():
    return template('deleteMenu.html', c = companyCursor)

@post('/deleteSuccess')
def deleteSuccess():
    return template('deleteSuccess.html', c = companyCursor, db = companyDb)

@route('/departmentView')
def departmentView():
    return template('departmentView.html', c = companyCursor)

@route('/statistics')
def statistics():
    return template('statistics.html')

@route('/average')
def average():
    return template('average.html', c = companyCursor)

@post('/averageResult')
def averageResult():
    return template('averageResult.html', c = companyCursor)

@route('/genders')
def Genders():
    return template('genders.html', c = companyCursor)

@route('/male')
def Male():
    return template('male.html', c = companyCursor)

@route('/female')
def Female():
    return template('female.html', c = companyCursor)

@route('/other')
def Other():
    return template('other.html', c = companyCursor)

@route('/attendance')
def attendanceStat():
    return template('attendance.html', c = companyCursor)

@post('/attendanceResult')
def attendanceResult():
    return template('attendanceResult', c = companyCursor)

@route('/groupBy')
def groupBy():
    return template('groupBy.html', c = companyCursor)

@post('/groupByResult')
def groupByResult():
    return template('groupByResult.html', c = companyCursor)

@route('/OldEmployees')
def OldEmployees():
    return template('OldEmployee.html', c = companyCursor)

@route('/howMany')
def howMany():
    return template('howMany.html', c = companyCursor)

@post('/howManyResult')
def howManyResult():
    return template('howManyResult.html', c = companyCursor)




@error(404)
def error404(error):
    return template('404.html')

@error(405)
def error405(error):
    return template('405.html')

@error(500)
def error500(error):
    return template('500.html')




application = default_app()






