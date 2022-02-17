!!!WELCOME TO SNOW-AUTOREMEDIATION REPO!!!
 
1. Introduction

This repository contains many project files and undertakings as part of Learning and Experiment on Service Now Orchestration and Automated Incident Handling. There are reusable code in the folders to automate the flow of events into a servicenow instance and the update sets folder contain the xml files with different flows written to automate playbooks (eg. in the playbooks folder) running on servers.



2. Inventory and Snow Instance

The code and flows have been made in a reusable manner so the part of the instance name and the target/control machine details are all configurable.
For now, the project has been configured on free to use infra (on Azure) and developer instances provided by Service Now.
Snow instance - https://dev120649.service-now.com/
Control server - remotews01.southindia.cloudapp.azure.com
Target systems - remotews02.southindia.cloudapp.azure.com, remotews03.southindia.cloudapp.azure.com



3. Configuring the INI Files
Inside the folders 1 and 2 there are ini files named "EventcfgAuto.ini" and "EventcfgMan.ini". These values can be changed to get desired type of simulated events into your instance.
There are currently two REST ways to push the Events 

a) Through MID Server - https://docs.servicenow.com/bundle/sandiego-it-operations-management/page/product/event-management/task/send-events-via-web-service.html\
b) Directly to the instance - https://docs.servicenow.com/bundle/sandiego-it-operations-management/page/product/event-management/concept/event-collection-via-MID-using-push.html\

The automated approach uses opt (a) and Manual one uses opt (b)
Instructions to configure the ini files are given as comments in the files



2. Folder Contents

"1 - Automated Event Generator"

    Contains a python code to push events into a snow demo instance specified in the cfg file. CFG file contains the fields needed to be populated for the events. Script randomly picks a value from the array of values provided
    The script in this folder will run on an automated schedule to maintain constant flow of events into snow instance

"2 - Manual Event Generator"

    Contains a python code to push events into a snow demo instance specified in the cfg file. CFG file contains the fields needed to be populated for the events. Enter only one value which needs to be passed in the event
    The script has to be triggered manually

"3 - Update Sets - Backup"

    Contains the backup of update sets so that any work can be easily replicated instance to instance

"4 - Playbooks"

    Contains the remedition playbooks written to be called and the inventory file to be used

"Certificates"

    Self-Signed Certificates to use for communication to Mid-Server
