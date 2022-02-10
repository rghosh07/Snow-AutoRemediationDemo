from random import choice
# from sys import argv
from requests import post
from requests.auth import HTTPBasicAuth
import configparser
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config=configparser.ConfigParser(interpolation=None)
config.read('EventcfgMan.ini')

payload={"records":[{"source":config['Event Details']['source'], "event_class":config['Event Details']['source']+" 10.0.0.4","node":config['Event Details']['node'],"metric_name":config['Event Details']['metric'], "severity":config['Event Details']['severity'], "description":config['Event Details']['description'],"additional_info": {"prom-severity": "High", "os_type":"RedHat Enterprise linux 8"}}]}
print(payload)
print(config['ServiceNow Instance'].getboolean('midserver_event_collection'))

if config['ServiceNow Instance'].getboolean('midserver_event_collection'):
    url="http://{}:{}/api/mid/em/jsonv2".format(config['ServiceNow Instance']['mid_ip'],config['ServiceNow Instance']['mid_port'])

elif not config['ServiceNow Instance'].getboolean('midserver_event_collection'):
    url="https://{}.service-now.com/api/global/em/jsonv2".format(config['ServiceNow Instance']['yourInstance'])

else:
    print("Error: midserver_event_collection parameter not confuigured correctly")
    exit(1)

print(url)

headers={"Content-Type": "application/json"}
response = post(url, data=str(payload), headers=headers, verify=False, auth=HTTPBasicAuth('rghosh','Turtle$123'))
print(response.text)
