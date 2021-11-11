# Home-Assistant Python Scripts
Python Scripts for Home-Assistant (http://www.home-assistant.io)

# Zyxel-NSA310-Home-Assistant Monitoring

This is a python script to grab data from Zyxel NSA310 NAS and display in Home Asisstant as sensors.
The script is connecting to the WEB UI and take:
- CPU Usage
- CPU Temp
- HDD Health
- HDD Usage
- Memory Usage
    
  ![image](https://user-images.githubusercontent.com/33951255/141298155-88b4dd31-f653-4d78-92b6-1715e7d80b73.png)
  
  
 And create a JSON for Home Asistant Sensor:
 { "cpu_usage": 0, "cpu_temp": "42.00", "mem_usage": "22", "hdd_usage": "47", "hdd_health": "healthy" }

![image](https://user-images.githubusercontent.com/33951255/141294137-3b36bab4-a8db-4bb9-9fb6-f17acf25f64e.png)

**** This is not an official integration.


# Working Model and firmware version:

Model Name NSA310
Firmware Version V4.70(AFK.3)

Depending on your firmware version this script can be ajusted.
What I saw on different version the link is different, for example mine is $IP/r49435/

![image](https://user-images.githubusercontent.com/33951255/141297059-c6c8eaf9-51ea-4be4-a4e9-fa51921e7f5c.png)


### Installation
* If not exist, in /config/python_scripts/ create a file called nsa310_get_info.py 
* Copy the code inside.
* Configure with config below.
* Restart Home-Assistant.

### Usage
To use this sensor add the following to your sensors.yaml file:

### Example sensors.yaml entry
Please change the $IP $USERNAME $PASSWORD with your NSA ip, username and password used to login to the NSA.

```
- platform: command_line
  name: nsa310
  json_attributes:
    - cpu_usage
    - cpu_temp
    - mem_usage
    - hdd_usage
    - hdd_health
  command: python3 /config/python_scripts/nsa310_get_info.py $IP $USERNAME $PASSWORD
  value_template: '{{ value_json.cpu_usage }}'
  unit_of_measurement: "%"
  scan_interval: 60
  
  - platform: template  
  sensors:
    cpu_temp:
      friendly_name: 'NSA310 CPU Temp' 
      value_template: '{{ states.sensor.nsa310.attributes.cpu_temp }}'
      unit_of_measurement: "°C"
    mem_usage:
      friendly_name: 'NSA310 Memory Usage' 
      value_template: '{{ states.sensor.nsa310.attributes.mem_usage }}'
      unit_of_measurement: "%"
    hdd_usage:
      friendly_name: 'NSA310 HDD Usage' 
      value_template: '{{ states.sensor.nsa310.attributes.hdd_usage }}'
      unit_of_measurement: "%"  
    hdd_health:
      friendly_name: 'NSA310 HDD Health' 
      value_template: '{{ states.sensor.nsa310.attributes.hdd_health }}'
```

![image](https://user-images.githubusercontent.com/33951255/141295722-c36c4ea3-3eae-4f74-81ec-b4452790f0d3.png)

