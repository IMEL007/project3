import os

from flask import Flask, render_template, request
import smtplib
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
OWN_EMAIL = "TImjes007@gmail.com"
OWN_PASSWORD = "ijfiqfzzfqvetqcb"
app = Flask(__name__)



@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

@app.route("/post")
def post():
    return render_template("post.html")



if __name__ == "__main__":
    app.run(debug=True)