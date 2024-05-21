'''A Flask web server for a developer portfolio website.'''
from flask import Flask, render_template, redirect, request
from emailer import Emailer

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # send email
        emailer = Emailer()
        if emailer.send_email('andrewvanderleest@gmail.com',
                            message=f'''Subject:New message from portfolio website\n
                            Sender: {fname} {lname}\n
                            Email addr: {email}\n
                            Subject: {subject}\n
                            Message: {message}'''):

            # display contacted message on index redirect
            contact_header = "Your message has been sent. You will hear back from me soon. Thank you!"

        else:
            contact_header = "Failed to send message, please try again later."

    else:
        contact_header = 'Contact'
    
    return render_template('index.html', contact_header=contact_header)

if __name__ == "__main__":
    app.run(debug=True)