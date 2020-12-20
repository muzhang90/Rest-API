


device_ip='10.85.168.43'

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint



def rest_api_json(ip):

    my_headers = { 'Content-Type': 'application/xml','Accept': 'application/json'}
    r = requests.get(f'http://{ip}:3000/rpc/get-chassis-inventory', auth=HTTPBasicAuth('labroot', 'lab123'), headers=my_headers)
    pprint(r.json())

def rest_api_xml(ip):
    my_headers = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}
    r = requests.get(f'http://{ip}:3000/rpc/get-chassis-inventory', auth=HTTPBasicAuth('labroot', 'lab123'),
                     headers=my_headers)
    print(r.content.decode('utf-8'))


def rest_api_plain_text(ip):
    my_headers = {'Content-Type': 'application/xml', 'Accept': 'text/plain'}
    r = requests.get(f'http://{ip}:3000/rpc/get-chassis-inventory', auth=HTTPBasicAuth('labroot', 'lab123'),
                     headers=my_headers)
    print(r.content.decode('utf-8'))

if __name__ == '__main__':
    print('Use Rest API to get chassis informatin:\n\n')
    print('*'*100)
    print('Json format')
    rest_api_json(device_ip)
    print('*'*100)
    print('XML format')
    rest_api_xml(device_ip)
    print('*' * 100)
    print('Text format')
    rest_api_plain_text(device_ip)