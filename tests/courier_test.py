# stdlib
import unittest
import os
import re
import shutil

# 3rd party
from flexmock import flexmock

# artisan
import envelopes
import courier


class CourierTest(unittest.TestCase):
    """
    Test individual methods in courier class.
    """

    @classmethod
    def setUpClass(cls):
        # Set environ variables for Courier to use
        os.environ["EMAIL_SRVC_HOST"] = "smtp.mandrillapp.com"
        os.environ["EMAIL_SRVC_PORT"] = "25"
        os.environ["EMAIL_SRVC_LOGIN"] = "admin@firstopinion.co"
        os.environ["EMAIL_SRVC_PASSWORD"] = "ho_socIk5NarJ_KXoC800g"
        os.environ["EMAIL_FROM_ADRESS"] = "info@firstopinion.co"
        os.environ["EMAIL_TMPL_ROOT"] = "/vagrant/tests/email"
        # Make test directory
        cls.test_dir = os.path.join(os.environ["EMAIL_TMPL_ROOT"], 'test')
        os.makedirs(cls.test_dir)

    @classmethod
    def tearDownClass(cls):
        # Clean up by removing dir
        shutil.rmtree(os.environ["EMAIL_TMPL_ROOT"])

        # Delete environ variables as they are no longer in use
        del os.environ["EMAIL_SRVC_HOST"]
        del os.environ["EMAIL_SRVC_PORT"]
        del os.environ["EMAIL_SRVC_LOGIN"]
        del os.environ["EMAIL_SRVC_PASSWORD"]
        del os.environ["EMAIL_FROM_ADRESS"]
        del os.environ["EMAIL_TMPL_ROOT"]

    def test_send(self):
        # Message Params
        TO_ADDRESS = "admin@firstopinion.co"
        SUBJECT = "test"
        MESSAGE_NAME = "test"
        # Template html
        file_html = """
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1>Hello {{ name }}</h1>
                </body>
            </html>
        """
        # Template txt
        file_txt = """Hello {{ name }}"""

        # Expected output html 
        out_html = """
            <html>
                <head>
                    <title>Test</title>
                </head>
                <body>
                    <h1>Hello Courier</h1>
                </body>
            </html>
        """
        # Expected output txt
        out_txt = """Hello Courier"""

        # Add html file
        html_file = os.path.join(self.test_dir, 'index.html')
        with open(html_file, 'w') as file:
            file.write(file_html)
        # Add txt file
        txt_file = os.path.join(self.test_dir, 'index.txt')
        with open(txt_file, 'w') as file:
            file.write(file_txt)

        # Mock send method that checks if output is correct
        def mock_send(this, *args, **kwargs):
            # cache out values
            result_txt = this._parts[0][1]
            result_html = this._parts[1][1]

            # normalize results
            whitespace_between_tags = re.compile('>\s*<',)
            expected_html = whitespace_between_tags.sub('><', out_html).strip()
            expected_txt = whitespace_between_tags.sub('><', out_txt).strip()
            result_html = whitespace_between_tags.sub('><', result_html).strip()
            result_txt = whitespace_between_tags.sub('><', result_txt).strip()

            # tests that output is expected
            self.assertEqual(expected_html, result_html)
            self.assertEqual(TO_ADDRESS, this._to[0])
            self.assertEqual(SUBJECT, this._subject)

        # Mock the method
        # flexmock(courier.Envelope, send=mock_send)    
        courier.Envelope.send = mock_send

        # init
        new_email = courier.Courier(TO_ADDRESS, SUBJECT, MESSAGE_NAME, {
            "name": "Courier"
        })


def suite():
    """
    Gather all the tests from this module in a test suite.
    """

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(CourierTest))
    return test_suite


# Execute from command line
if __name__ == "__main__":
    unittest.main()
