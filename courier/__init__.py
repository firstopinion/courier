# stdlib
import os

# 3rd party
# import envelopes
from envelopes import Envelope
from jinja2 import Environment


class Courier(object):
    """
    Grab template, insert user data, and send
    """

    def __init__(self, to_addr, subject, message_name, data, tls=True):
        self.jinja = Environment()
        self.creds = {
            "host": os.environ["EMAIL_SRVC_HOST"],
            "port": int(os.environ["EMAIL_SRVC_PORT"]),
            "login": os.environ["EMAIL_SRVC_LOGIN"],
            "password": os.environ["EMAIL_SRVC_PASSWORD"],
            "tls": tls
        }
        self.msg = {
            "from_addr": os.environ["EMAIL_FROM_ADRESS"],
            "to_addr": to_addr,
            "subject": subject
        }
        # Loop over msg directory and template html and txt
        message_dir = os.path.join(os.environ["EMAIL_TMPL_ROOT"], message_name)
        for file_name in os.listdir(message_dir):
            file_path = os.path.join(message_dir, file_name)
            if file_path.endswith(".html"):
                self.msg["html_body"] = self.template(file_path, data)
            elif file_path.endswith(".txt"):
                self.msg["text_body"] = self.template(file_path, data)

    def send(self):
        """
        Init envelope by passing message details and send
        using credentials define during self init
        """
        envelope = Envelope(**self.msg)
        envelope.send(**self.creds)

    def template(self, path, data):
        """
        Open provided file and render with passed data
        """
        with open(path, 'r') as file:
            tmpl = self.jinja.from_string(file.read())
            return tmpl.render(**data)
