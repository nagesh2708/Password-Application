import smtplib

def connection(reciever,passcode):
    sender = 'teamingteams@gmail.com'
    password = '123@Hasher#'
    message = '''From: Password Saver Application
    <teamingteams@gmail.com>
    To: To Person <''' + reciever + '''>
    Subject : Resending Password

    Password: '''+passcode

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,reciever,message)