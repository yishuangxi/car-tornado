import re

re_username = re.compile(r'^[a-zA-Z_][a-zA-Z0-9]{1,10}$')

m = re_username.match('1abcd123')

print m