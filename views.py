from package import urls,unic
from flask import request,render_template,redirect,flash
from models import db,Landsat7,Landsat8,Landsat9
from datetime import datetime
from werkzeug.exceptions import BadRequestKeyError
import report_msg

def index7():
    if request.method == "POST":
        try:
            date = f'{datetime.now().year}:{datetime.now().month}:{datetime.now().day}'
            requestuser = Landsat7(
            code = unic(),
            band1 = request.form['L7band1'],
            band2 = request.form['L7band2'],
            band3 = request.form['L7band3'], 
            band4 = request.form['L7band4'],
            band5 = request.form['L7band5'],
            band6 = request.form['L7band6'],
            band7 = request.form['L7band7'], 
            city = request.form['city'],
            date = date,
            takmili = request.form['text'],
            )
            db.session.add(requestuser)
            db.session.commit()
            msg = f"{report_msg.sus_res} :) {requestuser.code}"
            return render_template('index7.html',report=msg,context=urls)
        except BadRequestKeyError:
            return render_template('index7.html',report=report_msg.err_res,context=urls)
    return render_template('index7.html',context=urls)

def index8():
    if request.method == "POST":
        try:
            date = f'{datetime.now().year}:{datetime.now().month}:{datetime.now().day}'
            requestuser = Landsat8(
            code = unic(),
            band1 = request.form['L8band1'],
            band2 = request.form['L8band2'],
            band3 = request.form['L8band3'],
            band4 = request.form['L8band4'],
            band5 = request.form['L8band5'],
            band6 = request.form['L8band6'],
            band7 = request.form['L8band7'],
            city = request.form['city'],
            date = date,
            takmili = request.form['text'],
            )
            db.session.add(requestuser)
            db.session.commit()
            msg = f"{report_msg.sus_res} <---> {requestuser.code} "
            return render_template('index8.html',report=msg,context=urls)
        except BadRequestKeyError:
            return render_template('index8.html',report=report_msg.err_res,context=urls)
    return render_template('index8.html',context=urls)

def index9():
    if request.method == "POST":
        try:
            date = f'{datetime.now().year}:{datetime.now().month}:{datetime.now().day}'
            requestuser = Landsat9(
            code = unic(),
            band1 = request.form['L9band1'],
            band2 = request.form['L9band2'],
            band3 = request.form['L9band3'],
            band4 = request.form['L9band4'],
            band5 = request.form['L9band5'],
            band6 = request.form['L9band6'],
            band7 = request.form['L9band7'],
            city = request.form['city'],
            date = date,
            takmili = request.form['text'],
            )
            db.session.add(requestuser)
            db.session.commit()
            msg = f"{report_msg.sus_res} :) {requestuser.code}"
            return render_template('index9.html',report=msg,context=urls)
        except BadRequestKeyError:
            return render_template('index9.html',report=report_msg.err_res,context=urls)
    return render_template('index9.html',context=urls)

def admin():
    if request.method == "POST":
        admin = str(request.form["Admin"])
        pasw = str(request.form["Password"])
        if admin == "mobin_iran_doust":
            if pasw == "mobin_iran_doustmobin_iran_doust1380":
                user_7 = db.session.execute(db.select(Landsat7).order_by(Landsat7.id)).scalars().all()
                user_8 = db.session.execute(db.select(Landsat8).order_by(Landsat8.id)).scalars().all()
                user_9 = db.session.execute(db.select(Landsat9).order_by(Landsat9.id)).scalars().all()
                return render_template('AdminActivate.html',user7=user_7,user8=user_8,user9=user_9)
    return render_template('Admin.html')

def del_user_id7(name):
    select = name
    request_user = db.get_or_404(Landsat7,select)
    db.session.delete(request_user)
    db.session.commit()
    return f"{report_msg.delete}"

def del_user_id8(name):
    select = name
    request_user = db.get_or_404(Landsat8,select)
    db.session.delete(request_user)
    db.session.commit()
    return f"{report_msg.delete}"

def del_user_id9(name):
    select = name
    request_user = db.get_or_404(Landsat9,select)
    db.session.delete(request_user)
    db.session.commit()
    return f"{report_msg.delete}"

def get_code():
    if request.method == "POST":
        try:
            codes = int(request.form['codes'])
            f = db.session.execute(db.select(Landsat7).order_by(Landsat7.id)).scalars().all()
            o = db.session.execute(db.select(Landsat8).order_by(Landsat8.id)).scalars().all()
            x = db.session.execute(db.select(Landsat9).order_by(Landsat9.id)).scalars().all()
            num = [me for i in (f,o,x) for me in i if codes == me.code]
            if num == []:
                return '<button style=\'all:unset;color:red;font-size:25px\' onclick="history.back()">برگشتن-کد پیگیری تون اشتباه است</button>'
            return render_template("get_code.html",context=num)
        except ValueError:
            return render_template("get_code.html")
    return render_template("get_code.html")

def gcup():
    if request.method == "POST":
        _id = int(request.form["code"])
        link = request.form["link"]
        lib = request.form["lib"]
        if lib == "Landsat7":
            request_admin = db.get_or_404(Landsat7,int(_id))
            request_admin.link_dl = link
            db.session.commit()
            return "<script>history.back()</script>"
        elif lib == "Landsat8":
            request_admin = db.get_or_404(Landsat8,_id)
            request_admin.link_dl = link
            return "<script>history.back()</script>"
        elif lib == "Landsat9":
            request_admin = db.get_or_404(Landsat9,_id)
            request_admin.link_dl = link
            db.session.commit()
            return "<script>history.back()</script>"
    if request.method == "GET":
        return "404"