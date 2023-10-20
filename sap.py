from flask import Flask,render_template
sap=Flask(__name__)
@sap.route("/")
def devil():
    return
render_template("index.html")
if __name__=="__main__":
    sap.run(debug=True,port=3000)
    