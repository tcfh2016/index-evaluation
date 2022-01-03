import requests

r = requests.get('https://danjuanfunds.com/djmodule/value-center?channel=1300100141')
#r = requests.get('https://www.baidu.com')

print(r.status_code )
