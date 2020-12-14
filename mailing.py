import smtplib

def connection(reciever,passcode):
    sender = 'your mail'
    password = 'Your Password'
    message = '''From: Password Saver Application
    <Yourmail>
    To: To Person <''' + reciever + '''>
    Subject : Resending Password

    Password: '''+passcode

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,reciever,message)
