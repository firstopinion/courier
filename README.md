courier [![Build Status](https://travis-ci.org/firstopinion/courier.png)](https://travis-ci.org/firstopinion/courier)
=======

Prepare and send emails using jinja2, and envelopes.

![Courier](http://i.cloudup.com/m2vPQZ1ppj.jpg)



Installation
------------

Installing from source:

    python setup.py install


Setup
-----

Courier uses environment variables to send emails. The following need to be set.

| Name                | Example              |
| ------------------- | -------------------- |
| EMAIL_SRVC_HOST     | smtp.mandrillapp.com |
| EMAIL_SRVC_PORT     | 25                   |
| EMAIL_SRVC_LOGIN    | karlmalone@nba.com   |
| EMAIL_SRVC_PASSWORD | password             |
| EMAIL_FROM_ADRESS   | mailman@nba.com      |
| EMAIL_TMPL_ROOT     | /emails              |

Courier is meant to work hand in hand with [Artisan](https://github.com/firstopinion/artisan) builds and will look inside of the directory specified by the environemnt variable `EMAIL_TMPL_ROOT` for the following structure.

** EXAMPLE **

    - emails
        - welcome
            - index.html
            - index.txt
        - success
            - index.html
            - index.txt


Usage
-----

    from courier import Courier
    
    new_email = courier.Courier(TO_ADDRESS, SUBJECT, MESSAGE_NAME, DATA)

**EXAMPLE**

    from courier import Courier
    
    new_email = courier.Courier('karlmalone@nba.com', 'Special Delivery', 'success', {
        "first_name": "Karl",
        "last_name": "Malone"
    })

Tests
-----

    python setup.py test



Developing
----------

    python setup.py develop



License
-------

The MIT License (MIT)
Copyright (c) 2013 First Opinion

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
