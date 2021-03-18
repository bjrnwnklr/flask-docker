import os

# create a random secret key using 
#   import secrets
#   print(secrets.token_hex())
#
# or a random passphrase from http://useapassphrase.com
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cheesy-iodize-wildness-eject'
