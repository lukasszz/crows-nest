import urllib

import requests

xml = '<?xml version="1.0" encoding="UTF-8"?>  ' \
      '<request protocol="SmesX" version="2.2" user="" password="">    ' \
      ' <send_sms>      ' \
      '     <msisdn>697762400</msisdn>      ' \
      '             <body>[crow-nest] Test alertu sms</body>   ' \
      ' </send_sms>' \
      '</request>'

headers = {}
r = requests.post('', data={'xml': xml})
print(r.status_code)
print(r.text)
# urllib.parse.quote(xml)