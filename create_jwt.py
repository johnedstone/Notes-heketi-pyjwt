#!/usr/bin/env python
# https://github.com/heketi/heketi/wiki/API#authentication
# https://pyjwt.readthedocs.io/en/latest/
# https://github.com/jpadilla/pyjwt

import jwt
import datetime
import hashlib
import os

method = 'POST'
method = 'GET'
uri = '/clusters'
uri = '/clusters/29d9b388acbbb4b67487966da9c03597'
uri = '/volumes'
secret = os.getenv('SECRET', 'My Secret or something like that')

claims = {}

# Issuer
claims['iss'] = 'admin'

# Issued at time
claims['iat'] = datetime.datetime.utcnow() - datetime.timedelta(days=1)

# Expiration time
claims['exp'] = datetime.datetime.utcnow() \
              + datetime.timedelta(days=1000000)
              # + datetime.timedelta(minutes=10)

# URI tampering protection
encoded_string = '{}&{}'.format(method, uri).encode('utf-8')
# claims['qsh'] = hashlib.sha256(method + '&' + uri).hexdigest()
claims['qsh'] = hashlib.sha256(encoded_string).hexdigest()

print(jwt.encode(claims, secret, algorithm='HS256'))
