import textfsm
import requests
from requests.auth import HTTPBasicAuth

from pprint import pprint


device_ip='10.85.168.43'



def rest_api_get_interface_information(ip):
    my_headers = {'Content-Type': 'application/xml',  'Accept': 'text/plain'}
    r = requests.get(f'http://{ip}:3000/rpc/get-interface-information', auth=HTTPBasicAuth('labroot', 'lab123'),
                     headers=my_headers)
    return r.content.decode('utf-8')


def process_textfsm(str):
    template=textfsm.TextFSM(open('show_interface.textfsm'))
    int_data=template.ParseText(str)
    return (template.header,int_data)

if __name__ =='__main__':

    format_outout=process_textfsm(rest_api_get_interface_information(device_ip))
    print(format_outout[0])
    pprint(sorted(format_outout[1],key=lambda x: x[1],reverse=True))