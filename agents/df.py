import shutil

import requests

freeGiB = round(shutil.disk_usage('/home').free / 1024 ** 3)

if freeGiB < 50:
    status = 'Error'
else:
    status = 'OK'

r = requests.post('http://127.0.0.1:5000/report', json={"agent": 'df', "status": status, "desc": '/home ' + str(freeGiB) + ' GiB'})
print(r.status_code)

