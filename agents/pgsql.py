import os
import requests

stream = os.popen('ls -l')
output = stream.read()

r = requests.post('http://127.0.0.1:5000/report', json={"desc": output})
print(r.status_code)
# print(r.json())

