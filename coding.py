from flask import *
app=Flask(__name__)
from src.dbconnection import *
app.secret_key='123'
import functools

def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('loginindex.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



@app.route('/')
def log():
    return render_template('loginindex.html')

@app.route("/login",methods=['get','post'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="SELECT * FROM login WHERE username=%s AND password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invaild");window.location="/"</script>'''
    elif res['type']=='admin':
        session['lid'] = res['id']
        return '''<script>alert("welcome to adminhome");window.location="adminindex"</script>'''
    elif res['type'] == 'staff':
        session['lid'] = res['id']
        return '''<script>alert("welcome to staffhome ");window.location="staffindex"</script>'''
    elif res['type'] == 'student':
        session['lid'] = res['id']
        return '''<script>alert("welcome to studenthome");window.location="studentindex"</script>'''
    else:
        return '''<script>alert("invaild");window.location="/"</script>'''
@app.route('/stureg')
def stureg():
    qr="SELECT * FROM `course`"
    r=selectall(qr)
    return render_template('reg student.html',val=r)

@app.route('/sturegister',methods=['post'])
def sturegister():
    fname=request.form['textfield']
    lname = request.form['textfield2']
    gender = request.form['radiobutton']
    course = request.form['select']
    place = request.form['textfield5']
    post = request.form['textfield6']
    pin= request.form['textfield7']
    phone = request.form['textfield8']
    email = request.form['textfield9']
    uname = request.form['textfield10']
    pwrd = request.form['textfield11']
    q="INSERT INTO `login`VALUES(NULL,%s,%s,'pending')"
    v=(uname,pwrd)
    id=iud(q,v)
    qry="insert into `student` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),course,fname,lname,gender,place,post,pin,phone,email)
    iud(qry,val)
    return'''<script>alert("added");window.location="/"</script>'''

"============================================================================================================"
@app.route("/adminindex")
@login_required
def adminindex():
    return render_template('admin/adminindex.html')


@app.route("/addandmanastaff")
@login_required
def addandmanastaff():
    q="SELECT * FROM staff"
    r=selectall(q)
    return render_template('admin/add amd manage staff.html',val=r)
@app.route("/addstaff",methods=['post'])
@login_required
def addstaff():
    return render_template('admin/add staff.html')
@app.route("/addstaff1",methods=['post'])
@login_required
def addstaff1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    place=request.form['textfield5']
    post=request.form['textfield6']
    pin=request.form['textfield7']
    phone=request.form['textfield8']
    email=request.form['textfield9']
    username=request.form['textfield10']
    password=request.form['textfield11']
    qry="insert into login values(null,%s,%s,'staff')"
    val=(username,password)
    id=iud(qry,val)
    qry1="INSERT INTO `staff`VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),fname,lname,gender,place,post,pin,phone,email)
    iud(qry1,val1)
    return '''<script>alert("added");window.location="addandmanastaff"</script>'''




@app.route("/deletestaff")
@login_required
def deletestaff():
    id=request.args.get('id')
    q="delete from staff where lid=%s "
    iud(q,id)
    qr="delete from login where id=%s"
    iud(qr,str(id))
    return '''<script>alert("deleted");window.location="addandmanastaff"</script>'''


@app.route("/editstaff")
@login_required
def editstaff():

    id = request.args.get('id')
    session['staffid']=id
    print("======",id)
    qry="select * from staff where  lid=%s"
    res=selectone(qry,id)

    return render_template('admin/edit staff..html',val=res)

@app.route('/edit_staff', methods=['post'])
@login_required
def edit_staff():
    print(request.form)
    f_name=request.form['textfield']
    l_name=request.form['textfield2']
    gender=request.form['radiobutton']
    place=request.form['textfield5']
    post=request.form['textfield6']
    pin=request.form['textfield7']
    phone=request.form['textfield8']
    email=request.form['textfield9']


    qry = "UPDATE `staff` SET `fname`=%s, `lname`=%s, `gender`=%s, `place`=%s, `post`=%s, `pin`=%s, `phone`=%s, `email`=%s WHERE `lid`=%s"
    val = (f_name,l_name,gender,place,post,pin,phone,email,session['staffid'])
    iud(qry,val)

    return '''<script>alert("Succefully edited");window.location="addandmanastaff"</script>'''


@app.route("/addandmanagscholar")
@login_required
def addandmanagscholar():

    qry="select * from scholarship"
    r=selectall(qry)
    return render_template('admin/add and ,manage sholarship.html',val=r)

@app.route("/addscholar",methods=['post'])
@login_required
def addscholar():
    return render_template('admin/add scholarship.html')

@app.route("/addscholar1",methods=['post'])
@login_required
def addscholar1():
    sho=request.form["textfield"]
    amo = request.form["textfield2"]
    de = request.form["textarea"]
    qry="INSERT INTO `scholarship`VALUES (NULL,%s,%s,%s,CURDATE())"
    val=(sho,amo,de)
    iud(qry,val)
    return '''<script>alert("Succefully added");window.location="addandmanagscholar"</script>'''

@app.route("/editscholar")
@login_required
def editscholar():
    id = request.args.get('id')
    session['id'] = id
    print("======", id)
    qry = "select * from scholarship where  id=%s"
    res = selectone(qry, id)
    return render_template('admin/edit  scholarship.html',val=res)

@app.route("/editscholar1",methods=['post'])
@login_required
def editscholar1():
    sho = request.form["textfield"]
    amo = request.form["textfield2"]
    de = request.form["textfield3"]
    qry="UPDATE `scholarship`SET `scholarship`=%s,`amount`=%s,`details`=%s,`date`= CURDATE()WHERE `id`=%s"
    val = (sho, amo, de,session['id'])
    iud(qry, val)
    return '''<script>alert("Succefully edited");window.location="addandmanagscholar"</script>'''

@app.route("/deletescholar")
@login_required
def deletescholar():
    id=request.args.get('id')
    qry=" DELETE FROM `scholarship` WHERE `id`=%s"
    iud(qry,id)
    return '''<script>alert("Succefully deteted");window.location="addandmanagscholar"</script>'''

@app.route("/addandmanagecourse")
@login_required
def addandmanagecourse():
    q="SELECT * FROM `course` "
    r=selectall(q)
    return render_template('admin/add and manage course.html',val=r)

@app.route("/addcourse",methods=['post'])
@login_required
def addcourse():
    return render_template('admin/add course.html')
@app.route("/addcourse1",methods=['post'])
@login_required
def addcourse1():
    cou = request.form['textfield']
    fee = request.form['textfield2']
    dur = request.form['textfield3']
    qry = "INSERT INTO `course`VALUES(NULL,%s,%s,%s)"
    val = (cou, fee, dur)
    iud(qry, val)
    return '''<script>alert("Succefully added");window.location="addandmanagecourse"</script>'''

@app.route("/editcourse")
@login_required
def editcourse():
    id = request.args.get('id')
    session['cid'] = id
    print("======", id)
    qry = "select * from course where  cid=%s"
    res = selectone(qry,id)

    return render_template('admin/edit course.html',val=res)
@app.route("/editcourse1",methods=['post'])
@login_required
def editcourse1():
    cou = request.form['textfield']
    fee = request.form['textfield2']
    dur = request.form['textfield3']
    qry="UPDATE `course`SET `course`=%s,`fee`=%s,`duration`=%s WHERE `cid`=%s"
    val= (cou, fee, dur,session['cid'])
    iud(qry, val)
    return '''<script>alert("Succefully edited");window.location="addandmanagecourse"</script>'''


@app.route("/deletecourse")
@login_required
def deletecourse():
    id = request.args.get('id')
    q = "DELETE FROM `course` WHERE `cid`=%s"
    iud(q, id)
    return '''<script>alert("Succefully deleted");window.location="addandmanagecourse"</script>'''



@app.route("/viewfeedback")
@login_required
def viewfeedback():
    q="SELECT `feedback`.*,`student`.`fname`,`lname` FROM `feedback`JOIN `student`ON `feedback`.`uid`=`student`.`id` "
    v=selectall(q)
    return render_template('admin/view feedback.html',val=v)


@app.route("/confirmapplication")
@login_required
def confirmapplication():

    q="SELECT `application`.`date`,`application`.`id`,application.status,`scholarship`.`scholarship`,`student`.`fname`,`lname`FROM `application` JOIN `scholarship`ON `application`.`sch_id`=`scholarship`.`id`JOIN `student`ON `student`.`lid`=`application`.`st_id` where application.status!='pending'"
    res=selectall(q)
    return render_template('admin/confirm application.html',val=res)

@app.route("/confirmapplication1")
@login_required
def confirmapplication1():
    id=request.args.get("id")
    qry="UPDATE `application`SET  `status`= 'confirm' WHERE `id`=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Succefully confirmed");window.location="confirmapplication"</script>'''

@app.route("/confirmapplication2")
@login_required
def confirmapplication2():
    id=request.args.get("id")
    qry="UPDATE `application`SET  `status`= 'rejected' WHERE `id`=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Succefully confirmed");window.location="confirmapplication"</script>'''

"=============================================================================================================================="


@app.route("/staffindex")
@login_required
def staffindex():
    return render_template('staff/staffindex.html')


@app.route("/addandmanagegovtsholar")
@login_required
def addandmanagegovtsholar():
    qry="SELECT * FROM `govt_scholarship`"
    r=selectall(qry)
    return render_template('staff/add and ,manage sholarship govt.html',val=r)


@app.route("/addgovtsho",methods=['post'])
@login_required
def addgovtsho():

    return render_template('staff/add govt scholarship.html')
@app.route("/addgovtsho1",methods=['post'])
@login_required
def addgovtsho1():
    sho=request.form["textfield"]
    amo = request.form["textfield2"]
    det = request.form["textfield3"]
    qry="insert into govt_scholarship values(null,%s,%s,%s,curdate())"
    val=(sho,amo,det)
    iud(qry,val)
    return '''<script>alert("Succefully added");window.location="addandmanagegovtsholar"</script>'''


@app.route("/editgovtshol")
@login_required
def editgovtshol():
    id=request.args.get('id')
    session['gid']=id
    qry="select * from govt_scholarship where gid=%s"
    res=selectone(qry,id)
    return render_template('staff/edit govt scholarship.html',val=res)
@app.route("/editgovtsho2",methods=['post'])
@login_required
def editgovtsho2():
    sho=request.form["textfield"]
    amo = request.form["textfield2"]
    det = request.form["textfield3"]
    qry="UPDATE `govt_scholarship`SET `scholarship`=%s,`amount`=%s,`details`=%s,`date`= CURDATE() WHERE `gid`=%s"
    val = (sho, amo, det,session['gid'])
    iud(qry, val)
    return '''<script>alert("Succefully edited");window.location="addandmanagegovtsholar"</script>'''
@app.route("/delegovtsho")
@login_required
def delegovtsho():
    id=request.args.get('id')
    q="DELETE FROM `govt_scholarship`WHERE `gid`=%s"
    iud(q,id)
    return '''<script>alert("Succefully deleted");window.location="addandmanagegovtsholar"</script>'''

@app.route("/forwardtoadmin")
@login_required
def forwardtoadmin():
    q = "SELECT `application`.*,`student`.*,`scholarship`.* FROM `application`JOIN`student` ON `student`.`lid`=`application`.`st_id` JOIN`scholarship` ON `scholarship`.`id`=`application`.`sch_id`  WHERE application.status='pending'   "
    r = selectall(q)
    return render_template('staff/forward to admin.html',val=r)

@app.route("/forwardtoadmin1")
@login_required
def forwardtoadmin1():
    id=request.args.get('id')
    q="UPDATE  `application`SET `status`='forwarded'where id=%s"
    v=(id)
    iud(q,v)
    return '''<script>alert("Succefully forwarded");window.location="forwardtoadmin"</script>'''


@app.route("/verifystudent")
@login_required
def verifystudent():
    qry="SELECT `student`.*,`login`.*,`course`.* FROM student JOIN `login` ON `login`.`id`=`student`.`lid`JOIN `course`ON `student`.`cid`=`course`.`cid` WHERE `login`.`type`='pending'"
    r=selectall(qry)
    return render_template('staff/verify student.html',val=r)

@app.route("/acceptstudent")
@login_required
def acceptstudent():
    id=request.args.get('id')
    qry="UPDATE `login`SET `type`='student' WHERE `id`= %s"

    iud(qry,str(id))
    return '''<script>alert("Succefully accepted");window.location="verifystudent"</script>'''

@app.route("/rejectstudent")
@login_required
def rejectstudent():
    id = request.args.get('id')
    qry = "UPDATE `login`SET `type`='rejected' WHERE `id`=%s"

    iud(qry, str(id))
    return '''<script>alert("Succefully rejected");window.location="verifystudent"</script>'''
@app.route("/viewsture")
@login_required
def viewsture():
    ry="SELECT `course`.*,`request`.*,`student`.* FROM `student`JOIN `request`ON `request`.`sid`=`student`.`lid`JOIN `course` ON `course`.`cid`=`request`.`cid` "
    res=selectall(ry)
    return render_template('staff/view stu request.html',vl=res)
@app.route("/acceptreuest")
@login_required
def acceptreuest():
    id=request.args.get('id')
    qry="UPDATE `request`SET `status`='confirm' WHERE `id`= %s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Succefully accepted");window.location="viewsture"</script>'''

@app.route("/rejectreuest")
@login_required
def rejectreuest():
    id = request.args.get('id')
    qry = "UPDATE `request`SET `status`='rejected' WHERE `id`=%s"
    val = (id)
    iud(qry, val)
    return '''<script>alert("Succefully rejected");window.location="viewsture"</script>'''


"=============================================================================================================================="

@app.route("/studentindex")
def studentindex():
    return render_template('student/studentindex.html')

@app.route("/applycourse")
@login_required
def applycourse():
    q="SELECT* FROM course "
    r=selectall(q)
    return render_template('student/apply for course.html',val=r)

@app.route("/applycourse1")
@login_required
def applycourse1():
    id=request.args.get('id')
    qr="SELECT * FROM `request` WHERE `sid`=%s AND `cid`=%s"
    v=(session['lid'],str(id))
    res=selectone(qr,v)
    if res is None:

        q="INSERT INTO `request`VALUES(NULL,%s,%s,'pending')"
        v=(session['lid'],id)
        iud(q,v)
        return '''<script>alert("Succefully apply ");window.location="applycourse"</script>'''
    else:
        return '''<script>alert("already applied ");window.location="applycourse"</script>'''



@app.route("/cheackstatusofapplication")
@login_required
def cheackstatusofapplication():

    qry="SELECT `application`.*,`scholarship`.* FROM `application`JOIN `scholarship`ON `scholarship`.`id`=`application`.`sch_id` WHERE `application`.`st_id`=%s "
    r=selectall2(qry,session['lid'])
    return render_template('student/cheak status of application.html',v=r)


@app.route("/cheackstatusofcourse")
@login_required
def cheackstatusofcourse():

    qry="SELECT `course`.*,`request`.* FROM `request`JOIN `course`ON `course`.`cid`=`request`.`cid`WHERE `request`.`sid`=%s"
    r=selectall2(qry,session['lid'])
    return render_template('student/view course request.html', v=r)
@app.route("/sendfeedback")
@login_required
def sendfeedback():
    return render_template('student/send feedback.html')
@app.route("/sendfeedback1",methods=['post'])
@login_required
def sendfeedback1():
    feed=request.form['textfield']

    qry="INSERT INTO `feedback`VALUES(NULL,%s,%s,CURDATE())"
    val=(session['lid'],feed)
    iud(qry,val)
    return '''<script>alert("Succefully sended");window.location="sendfeedback"</script>'''

# @app.route("/updategov")
# def updategov():
#     qry ="select * from  "
#     return render_template('student/update govstcholar.html')

@app.route("/viewscholarship")
@login_required
def viewscholarship():
    q="select * from govt_scholarship"
    res=selectall(q)
    return render_template('student/view scholarship.html',val=res)






@app.route("/updateadd")
@login_required
def updateadd():
    qry="SELECT DISTINCT (`scholarship`),`id`FROM `scholarship`"
    v=selectall(qry)
    return render_template('student/update add.html',v=v)

@app.route("/updateadinsert",methods=['post'])
@login_required
def updateadinsert():

    status = request.form['textfield']
    qry="UPDATE `application`SET  `status`=%s WHERE `st_id`=%s and status ='confirm'"
    val=(status,session['lid'])
    iud(qry,val)

    return '''<script>alert("Succefully updated");window.location="sendfeedback"</script>'''


@app.route("/viewupdatead")
@login_required
def viewupdatead():
    # id=request.args.get('id')
    # print(id,"=======================================")
    ry="SELECT `scholarship`.*,`application`.* FROM `scholarship`JOIN `application` ON `application`.`sch_id`=`scholarship`.`id`WHERE `status`='confirm 'and application.st_id=%s "
    res=selectall2(ry,session['lid'])
    return render_template('student/viewupdte.html',vl=res)

@app.route("/applyforscho")
@login_required
def applyforscho():
    qry="SELECT * FROM `scholarship`"
    res=selectall(qry)
    return render_template('student/apply scho.html',vl=res)


@app.route("/applyforscho1")
@login_required
def applyforscho1():
    id = request.args.get('id')
    q="SELECT * FROM `application` WHERE `sch_id`=%s AND `st_id`=%s"
    v=(str(id),session['lid'])
    res=selectone(q,v)
    if res is None:
        ry="INSERT INTO `application`VALUES(NULL,%s,%s,CURDATE(),'pending')"
        vl=(id,session['lid'])
        iud(ry,vl)
        return '''<script>alert("Applied Succefully");window.location="applyforscho"</script>'''
    else:
        return '''<script>alert("already applied ");window.location="applyforscho"</script>'''


"================================================================================================================================="




app.run(debug=True)
