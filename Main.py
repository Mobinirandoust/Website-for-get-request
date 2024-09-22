from flask import Flask,render_template
from models import db ,Landsat7,Landsat8,Landsat9
from package import urls
import views

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DAtabase.sqlite"

db.init_app(app)


with app.app_context():
    db.create_all()
    # codes = None
    # f = db.session.execute(db.select(Landsat7).order_by(Landsat7.id)).scalars().all()
    # o = db.session.execute(db.select(Landsat8).order_by(Landsat8.id)).scalars().all()
    # x = db.session.execute(db.select(Landsat9).order_by(Landsat9.id)).scalars().all()
    # print([codes for i in (f,o,x) for me in i if codes == me.code])
    # data = db.get_or_404(Landsat9,1)
    # print(data)

@app.route(urls['index'],methods=["GET","POST"])
def index():
    return render_template('index.html',context=urls)

app.add_url_rule(urls['land7'],"index7",views.index7,methods=["GET","POST"])
app.add_url_rule(urls['land8'],"index8",views.index8,methods=["GET","POST"])
app.add_url_rule(urls['land9'],"index9",views.index9,methods=["GET","POST"])
app.add_url_rule(urls['SuperUSer'],"admin",views.admin,methods=["GET","POST"])
app.add_url_rule(urls['del7'],"del_user_by_id7",views.del_user_id7,methods=["GET","POST"])
app.add_url_rule(urls['del8'],"del_user_by_id8",views.del_user_id8,methods=["GET","POST"])
app.add_url_rule(urls['del9'],"del_user_by_id9",views.del_user_id9,methods=["GET","POST"])
app.add_url_rule(urls['getcode'],"get_code",views.get_code,methods=["GET","POST"])
app.add_url_rule(urls["gcup"],"endgcup",views.gcup,methods=["GET","POST"])

@app.route(urls['get'])
def index_Error_404(name):
    return '<h1>Page 404 </h1> <button style=\'all:unset;color:red;font-size:25px\' onclick="history.back()">برگشتن</button>'

# if __name__=='__main__':
#     app.name = "anyraster"
#     app.debug = True
#     app.run()
#     pass