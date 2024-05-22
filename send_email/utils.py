import smtplib
from email.message import EmailMessage


class Email:
    HOST_PORT_TLS = 587
    HOST_PORT_SSL = 465
    has_attachment = False

    def __init__(self, email_host: str, email_host_user: str, email_host_password: str):
        self.email_host = email_host
        self.email_host_user = email_host_user
        self.email_host_password = email_host_password
        self.message = None

    def create_email_message(self, contacts: list, subject: str, content: str):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.email_host_user
        msg['To'] = ', '.join(contacts)
        msg.set_content(content)
        self.message = msg

    def to_html(self, file_path: str):
        with open(file_path, 'r') as html_file:
            html = html_file.read()
        self.add_alternative(html, subtype='html')

    def to_row_html(self, content: str):
        # content must be: """ </> """
        self.add_alternative(content, subtype='html')

    def add_image(self, file_path: str):
        with open(file_path, 'rb') as f:
            data = f.read()
            data_type = f.name.split('.')[-1]
            file_name = f.name
        self.add_attachment(data, maintype='image', subtype=data_type, filename=file_name)

    def add_pdf(self, file_path: str):
        with open(file_path, 'rb') as f:
            data = f.read()
            file_name = f.name
        self.add_attachment(data, maintype='application', subtype='octet-stream', filename=file_name)

    def add_alternative(self, file, subtype):
        if self.has_attachment:
            raise Exception('add_alternative must be called after add_attachment')
        self.message.add_alternative(file, subtype=subtype)

    def add_attachment(self, data, maintype, subtype, filename):
        self.has_attachment = True
        self.message.add_attachment(data, maintype=maintype, subtype=subtype, filename=filename)

    def send(self):
        if self.message:
            with smtplib.SMTP_SSL(self.email_host, self.HOST_PORT_SSL) as email:
                email.login(self.email_host_user, self.email_host_password)
                email.send_message(self.message)
        else:
            raise Exception('you must call create_email_message() ')

    def clear_email_message(self):
        self.message = None


class Gmail(Email):
    def __init__(self, *args, **kwargs):
        super().__init__(email_host="smtp.gmail.com", *args, **kwargs)

