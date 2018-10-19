from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")   #first visit to page
def index():
    return render_template("create_form.html")

@app.route("/success")   #no errors view
def display_success():
    user_name = request.args.get("user_name")
    return render_template("create_success_form.html", user_name=user_name)

@app.route("/", methods=["POST"])   #handles user errors
def signup_retry():

    user_name = request.form["user_name"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    user_name_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

#user name error

    if user_name == "":
        user_name_error = "That's not a valid username"

    if user_name.isalpha() == False:
        user_name_error = "That's not a valid username"

    if len(user_name) < 3 or len(user_name) > 20:
        user_name_error = "That's not a valid username"

# password error

    if password == "":
        password_error = "That's not a valid password"
        password = ""
    if password.isalpha() == False:
        password_error = "That's not a valid password"
        password = ""
    if len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"
        password = ""

# verify error
    if verify_password != password:
        verify_error = "Passwords do not match"
        verify_password = ""

# email error
    if email.count("@") != 1:
        email_error = "That's not a valid email"
    if email.count(".") != 1:
        email_error = "That's not a valid email"
    if email == "":
        email_error = ""

# errors corrected or show error messages

    if not user_name_error and not password_error and not verify_error and not email_error:
        return redirect("/success?user_name={0}".format(user_name))
    
    else:
        return render_template("create_form.html", user_name_error=user_name_error,
        password_error=password_error,
        verify_error=verify_error,
        email_error=email_error)


app.run()