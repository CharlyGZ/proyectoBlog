from flask import Flask
from flask import render_template

app = Flask(_name_)

@app.route("/")
def url_principal():
	return render_template("tem.html", nombre="Marco Armando")

	if _name_ == "_main_":
		app.run(debug= True)