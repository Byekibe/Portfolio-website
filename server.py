from crypt import methods
from flask import Flask, render_template, request, flash
import datetime as dt
import smtplib
from os import environ, path
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL="tariocreations22@yahoo.com"
# tariocreations@yahoo.com
APP_PASSWORD=environ.get("APP_PASSWORD")
# "usvvnkxjidibssrk"
year=dt.datetime.today().year


app=Flask(__name__)
app.config.from_object('config.ProdConfig')

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     return render_template("home.html", year=year)

@app.route("/")
def home():
    return render_template("home.html", year=year)

# @app.route("/inner")
# def inner():
#     return render_template("inner-page.html", year=year)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        name=request.form["name"]
        email=request.form["email"]
        subject=request.form["subject"]
        message=request.form["message"]

        send_email(name=name, email=email, subject=subject, message=message)
        return render_template("contact.html", msg_sent = True, year=year)
    return render_template("contact.html", year=year)
        
def send_email(name, email, subject, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage:{message}"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)
    return render_template("contact.html", year=year)

# @app.route("/porto")
# def port():
#     return render_template("portfolio-details.html", year=year)

@app.route("/services")
def services():
    return render_template("services.html", year=year)

@app.route("/about")
def about():
    return render_template("about.html", year=year)

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", year=year)

if __name__=="__main__":
    app.run(port=7000)