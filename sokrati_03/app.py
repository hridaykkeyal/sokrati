from flask import Flask, jsonify, request, abort, make_response, Response, render_template, session, redirect, url_for
import sendgrid
import os
from sendgrid.helpers.mail import *

app = Flask(__name__)

def send_email(to, password):
    sg = sendgrid.SendGridAPIClient(apikey="SENDGRID_API_KEY")
    from_email = Email("sokrati@gmail.com")
    to_email = Email(to)
    subject = "username and password"
    content = Content("text/plain", f'{to}: {password}')
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

@app.route('/')
def hello_world():
    return render_template('sokrati_03.html')

@app.route('/mail', methods=['POST'])
def mail():
    if request.method == 'POST':
        to = request.form['email']
        password = request.form['password']
        send_email(to, password)
    return 'username and password has been sent to your email address'

if __name__ == '__main__':
    app.run(debug = True)

