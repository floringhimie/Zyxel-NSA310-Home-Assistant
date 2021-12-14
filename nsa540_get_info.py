#!/usr/bin/python3
import requests
import re
import math
import time
import json 
import sys

ses = requests.session()
try:
    response_login = ses.get('http://192.168.1.130/r51209,/adv,/cgi-bin/weblogin.cgi?username='+str(sys.argv[1])+'&password='+str(sys.argv[2]))
    parse_login= response_login.text.split(':')[1].replace('}', '').replace(')', '')
    
    if parse_login == '9':
        response = ses.get('http://192.168.1.130/cmd,/ck6fup6/system_main/show_sysinfo?_dc=1')
        
        parse_json = json.loads(response.text)
        cpu_usage = str(parse_json["system"]["cpu"]["usage"].replace('%', '')).strip()
        cpu_temp = str(parse_json["system"]["status"]["temp"]).strip()
        mem_usage = str(parse_json["system"]["memory"]["usage"].replace('%', '')).strip()
        hdd_avail = str(parse_json["system"]["storageDetail"]["Available"]).strip()
        hdd_used_misc = str(parse_json["system"]["storageDetail"]["Misc"]).strip()
        hdd_used_photo = str(parse_json["system"]["storageDetail"]["Photos"]).strip()
        hdd_used_music = str(parse_json["system"]["storageDetail"]["Music"]).strip()
        hdd_used_video = str(parse_json["system"]["storageDetail"]["Video"]).strip()
        hdd_used_package = str(parse_json["system"]["storageDetail"]["Packages"]).strip()
        hdd_health = str(parse_json["system"]["status"]["sysStatus"]).strip()
            
    print('{ "cpu_usage": "'+cpu_usage+'", "cpu_temp": "'+cpu_temp+'", "mem_usage": "'+mem_usage+'", "hdd_avail": "'+hdd_avail+'", "hdd_used_misc": "'+hdd_used_misc+'", "hdd_used_photo": "'+hdd_used_photo+'", "hdd_used_music": "'+hdd_used_music+'", "hdd_used_video": "'+hdd_used_video+'", "hdd_used_package": "'+hdd_used_package+'", "hdd_health": "'+hdd_health+'" }')

    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
        }
    payload_data = "perform=logout"
    response_logout = ses.post('http://192.168.1.130/r51209,/adv,/cgi-bin/setuser.cgi', data=payload_data, headers=headers)
except:
    print('{}')
