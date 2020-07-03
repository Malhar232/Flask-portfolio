from flask import Flask, render_template, request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/<string:page_name>')
def redirect(page_name):
    return render_template(page_name)


@app.route('/form_submit', methods=['POST', 'GET'])
def form_submit():
    if request.method=="POST":
        try:
            data=request.form.to_dict()
            savedata(data)
            return redirect("/thankyou.html")
        except:
            return "Sorry could not save to database"

    else:
        return "Something is wrong buddy!"

def savedata(data):
    with open("database.csv",mode="a",newline='') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        spamwriter = csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.header()
        spamwriter.writerow([email,subject,message])