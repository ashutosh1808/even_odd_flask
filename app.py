from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/find")
def find():
	num=int(request.args.get("num"))
	res=""
	if num%2==0:
		res="Even"
	else:
		res="Odd"
	return render_template("home.html",msg=res)
if __name__=="__main__":
	app.run(debug=True,use_reloader=True)