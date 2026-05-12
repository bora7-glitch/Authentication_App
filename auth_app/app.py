from bottle import *
from sqlite3 import * 
import hashlib

def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()

def db_setup():
	con = None
	try:
		con = connect("auth.db")
		sql = "create table if not exists users(un varchar(30) primary key, pw varchar(100))"
		cursor = con.cursor()
		cursor.execute(sql)
		con.commit()
	except Exception as e:
		con.rollback()
		print("issue", e)
	finally:
		if con is not None:
			con.close()

db_setup()

application = Bottle()

@application.route("/", method=["GET", "POST"])
def login():
	if request.method == "POST":
		un = request.forms.get("un")
		pw = request.forms.get("pw")
		con = None
		try:
			con = connect("auth.db")
			sql = "select * from users where un = ? and pw = ?"
			cursor = con.cursor()
			hpw = hash_password(pw)
			cursor.execute(sql, (un, hpw))
			data = cursor.fetchone()
			if data:
				response.set_cookie("un", un, secret="kamalsirrocks")
			else:
				msg = "login failed"
				return template("login", msg=msg)
		except Exception as e:
			print("issue", e)
		finally:
			if con is not None:
				con.close()
		return redirect("home")
	else:
		return template("login", msg="")


@application.route("/signup", method=["GET", "POST"])
def signup():
	if request.method == "POST":
		un = request.forms.get("un")
		pw = request.forms.get("pw")
		cpw = request.forms.get("cpw")
		if pw == cpw:
			try:
				con = connect("auth.db")
				sql = "insert into users values(?,?)"
				cursor = con.cursor()
				hpw = hash_password(pw)
				cursor.execute(sql, (un, hpw))
				con.commit()
				msg = "registration complete"
				return template("signup", msg=msg)
			except Exception as e:
				con.rollback()
				msg = "user already exists" + str(e)
				return template("signup", msg=msg)
		else:
			msg = "password did not match"
			return template("signup", msg=msg)
	else:
		return template("signup", msg="")

@application.route("/home", method=["GET", "POST"])
def home():
	un = request.get_cookie("un", secret="kamalsirrocks")
	msg = "Welcome" + str(un)
	if un is None:
		redirect("/")
		
	if request.method == "POST":
		response.delete_cookie("un")
		return redirect("/")
	else:
		return template("home", msg=msg)

run(application, host="localhost", port=4050, debug=True, reloader=True)







