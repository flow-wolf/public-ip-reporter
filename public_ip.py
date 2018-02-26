import os
import sys
import json
import requests

#1) function to get response code, response headers, and data
def get_url(url,timeout):
    try:
        r = requests.get(url,timeout=timeout,allow_redirects=False)
    except requests.exceptions.RequestException as e:
        print (e)
        sys.exit(1)
    status_code = r.status_code
    resp_headers = r.headers
    data = r.json()
    return (status_code,dict(resp_headers),data)

#2) make the request
url = 'https://api.ipify.org?format=json'
timeout = 5
status_code,resp_headers,data = get_url(url,int(timeout))


print(status_code)
print(json.dumps(resp_headers,indent=4,sort_keys=False))
print(data)
ip = data['ip']


#3) write public ip to file
found_ip = ''
public_ip_file = 'public_ip.txt'
if os.path.isfile(public_ip_file):
    print("found file")
    file = open(public_ip_file, 'r') 
    found_ip = file.read()
else:
    file = open(public_ip_file,'w')
    file.write(ip)
    file.close()


#4) compare ip
if ip == found_ip:
    print('IPs are equal')
    print(ip,' ',found_ip)
else:
    print('IPs are not equal')
    file = open(public_ip_file,'w')
    file.write(ip)
    file.close()



