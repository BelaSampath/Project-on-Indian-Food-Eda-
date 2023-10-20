from flask import Flask,render_template
fap=Flask(__name__)

@fap.route("/")
def evil():
     return render_template("Index.html")
if __name__=="__main__":
    fap.run(debug=False,port=1200)