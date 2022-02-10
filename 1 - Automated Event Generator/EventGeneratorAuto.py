from random import choice, randrange
from requests import post
from requests.auth import HTTPBasicAuth
import configparser
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config=configparser.ConfigParser(interpolation=None)
config.read('EventcfgAuto.ini')

source = choice(config['Event Details']['sources'].split(','))
node = choice(config['Event Details']['nodes'].split(','))
metricLength = len(config['Event Details']['metrics'].split(','))
descLength = len(config['Event Details']['descriptions'].split(','))

if metricLength == descLength:
    metricChoiceInt = randrange(metricLength)
    metric = config['Event Details']['metrics'].split(',')[metricChoiceInt]
    description = config['Event Details']['descriptions'].split(',')[metricChoiceInt]
else:
    print("\nError: Please Check the Metric and Descriptions in config file EventcfgAuto.ini. Length doesn't match")
    exit(1)

severity = choice(config['Event Details']['severities'].split(','))
exAdd01 = choice(['High', 'Med', 'Low'])
exAdd02 = choice(['54', '76', '1', '32', '5'])
os_type = choice(["RedHat Enterprise linux 8", "RedHat Enterprise linux 7", "RedHat CentOS 7", "RedHat CentOS 8 gen 1", "Microsoft Windows Datacenter 2008", "Microsoft Windows Datacenter 2020"])
payload={"records":[{"source":source, "event_class":source+" 10.0.0.4","node":node,"metric_name":metric, "severity":severity, "description":description,"additional_info": {"example01_additional_info": exAdd01,"example02_additional_info": exAdd02, "os_type":os_type}}]}
print("\n",payload,"\n")

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