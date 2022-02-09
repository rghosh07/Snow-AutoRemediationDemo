
from random import choice
from sys import argv
from requests import post
from requests.auth import HTTPBasicAuth

Source="ITRS"
nodes=["813736b5841c.mylabserver.com", "813736b5842c.mylabserver.com"]
nodechoice=argv[1]
node=nodes[int(nodechoice)]

metrics=["Server Not Responding", "Service Stopped/Unresponsive"]
metricchoice=argv[2]
metric=metrics[int(metricchoice)] 

descriptions= ["Server "+str(node)+" is not responding. Please Check", "Mid Service is unresponsive on node "+str(node)+" . Please Check"]
description= descriptions[int(metricchoice)]

severity=choice(['Critical'])

payload={"records":[{"source":Source, "event_class":"PROM 2012 on prom.server.com","node":node,"metric_name":metric, "severity":severity, "description":description,"additional_info": {"prom-severity": "High", "os_type":"RedHat CentOS 8"}}]}
print(payload)

url="/api/mid/em/jsonv2"
headers={"Content-Type": "application/json"}
response = post(url, data=str(payload), headers=headers, verify=False, auth=HTTPBasicAuth('test','test'))
print(response.text)
