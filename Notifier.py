from email.mime.text import MIMEText
import smtplib
import sys

__author__ = 'novy'


class Notifier(object):
    def __init__(self, smtp_server, smtp_port, sender, destination, username, password):
        self.smtp_server, self.smtp_port, self.sender, self.destination = smtp_server, smtp_port, sender, destination
        self.username, self.password = username, password
        self.text_subtype = 'plain'
        self.subject = 'New grade in WD.'

    def notify_about_new_grade(self, grade_book_entry):
        content = "You've got a new grade!\n\n\n\n" + unicode(grade_book_entry).encode('utf-8')

        try:
            message = MIMEText(content, self.text_subtype, _charset="UTF-8")
            message['Subject'] = self.subject
            message['From'] = self.sender

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)

            try:
                server.sendmail(self.sender, self.destination, message.as_string())
            finally:
                server.close()

        except Exception, exc:
            sys.exit("mail failed; %s" % str(exc))



