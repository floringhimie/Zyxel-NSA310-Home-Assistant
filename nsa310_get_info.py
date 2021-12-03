#!/usr/bin/python3
import requests
import re
import math
import time
import json 
import sys

ses = requests.session()
try:
    response_login = ses.get('http://192.168.0.110/r49435,/adv,/cgi-bin/weblogin.cgi?username='+str(sys.argv[1])+'&password='+str(sys.argv[2]))
    parse_login= response_login.text.split(':')[1].replace('}', '').replace(')', '')
    
    if parse_login == '9':
        response = ses.get('http://192.168.0.110/r49435,/adv,/cgi-bin/zysh-cgi?c0=show cpu temperature&write=0&c1=show mem status&c2=storage showIVolumeInfo&c3=show cpu status')
        
        parse_json = response.text.replace('(', '').replace(')', '').replace("'", '"').replace(': [', '": [')
        parse_json = parse_json.replace('zyshd', '"zyshd')
        parse_json = parse_json.replace('errno0', '"errno0"').replace('errmsg0', '"errmsg0"')
        parse_json = parse_json.replace('errno1', '"errno1"').replace('errmsg1', '"errmsg1"')
        parse_json = parse_json.replace('errno2', '"errno2"').replace('errmsg2', '"errmsg2"')
        parse_json = parse_json.replace('errno3', '"errno3"').replace('errmsg3', '"errmsg3"')
        parse_json = json.loads(parse_json)
        
        cpu_usage = parse_json["zyshdata3"][0]["_CPU_utilization"].replace(' %', '')
        cpu_temp = parse_json["zyshdata0"][0]["_CPU_temperature"].replace('+', '').replace(' C', '')
        mem_usage = parse_json["zyshdata1"][0]["_memory_usage"].replace('%', '')
        hdd_usage = int(parse_json["zyshdata2"][0]["_TotalSpace"]) - int(parse_json["zyshdata2"][0]["_UsedSpace"])
        hdd_usage = round(100 - int(hdd_usage) / int(parse_json["zyshdata2"][0]["_TotalSpace"]) * 100) 
        hdd_health = parse_json["zyshdata2"][0]["_VolState"]
    
    print('{ "cpu_usage": '+str(cpu_usage)+', "cpu_temp": "'+str(cpu_temp)+'", "mem_usage": "'+str(mem_usage)+'", "hdd_usage": "'+str(hdd_usage)+'", "hdd_health": "'+str(hdd_health)+'" }')
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
        }
    payload_data = "perform=logout"
    response_logout = ses.post('http://192.168.0.110/r49435,/adv,/cgi-bin/setuser.cgi', data=payload_data, headers=headers)
except:
    print('{}')
