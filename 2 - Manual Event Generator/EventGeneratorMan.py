
from random import choice
# from sys import argv
from requests import post
from requests.auth import HTTPBasicAuth
import configparser
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config=configparser.ConfigParser()
config.read('EventcfgMan.ini')
# Source="ITRS"
# nodes=["813736b5841c.mylabserver.com", "813736b5842c.mylabserver.com"]
# nodechoice=argv[1]
# node=nodes[int(nodechoice)]

# metrics=["Server Not Responding", "Service Stopped/Unresponsive"]
# metricchoice=argv[2]
# metric=metrics[int(metricchoice)] 

# descriptions= ["Server "+str(node)+" is not responding. Please Check", "Mid Service is unresponsive on node "+str(node)+" . Please Check"]
# description= descriptions[int(metricchoice)]

# severity=choice(['Critical'])

payload={"records":[{"source":config['Event Details']['source'], "event_class":config['Event Details']['source']+" 10.0.0.4","node":config['Event Details']['node'],"metric_name":config['Event Details']['metric'], "severity":config['Event Details']['severity'], "description":config['Event Details']['description'],"additional_info": {"prom-severity": "High", "os_type":"RedHat Enterprise linux 8"}}]}
print(payload)

url=str(config['ServiceNow Instance']['url']+config['ServiceNow Instance']['api_path'])
print(url)
headers={"Content-Type": "application/json"}
response = post(url, data=str(payload), headers=headers, verify=False, auth=HTTPBasicAuth('rghosh','Turtle$123'))
print(response.text)
