from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Route to Home (Portfolio page)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the contact form submission
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Send email logic
        send_email(name, email, message)
        
        # Redirect to thank you page (or same page with success message)
        return redirect(url_for('index'))

def send_email(name, email, message):
    sender_email = "your-email@gmail.com"
    receiver_email = "your-email@gmail.com"  # Can be your email or someone else's for receiving messages
    password = "your-email-password"
    
    # Create the email content
    subject = "New Message from Portfolio Contact Form"
    body = f"New contact form submission:\n\nName: {name}\nEmail: {email}\nMessage:\n{message}"
    
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to Gmail's SMTP server (use SSL)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    app.run(debug=True)
