# Send Email

## Description
send email using SMTP in python

## Installation
To install the package, run the following command:
```sh
pip install git+https://github.com/SalarKesha/send-email.git
```

## Usage
```python
from send_email import Email
# Configuration
email_host = 'smtp.sample.com'
email_host_user: 'yourEmail@sample.com'
email_host_password: 'yourPassword'
contacts = ['receiver1@sample.com', 'receiver2@sample.com']
subject = 'sample subject'
content = 'sample content'
# Create and send email
email = Email(email_host, email_host_user, email_host_password)
email.create_email_message(contacts, subject, content)
email.send()
```
To send Gmail:
```python
from send_email import Gmail
gmail = Gmail(yourGmail, yourPassKey)
gmail.create_email_message(args)
gmail.send()
```


