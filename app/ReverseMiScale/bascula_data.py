from  app.ReverseMiScale.miScale import MiScale
import sys
import json

def get_json(scale):
    data_str = str(scale)
    data_json = json.loads(data_str)
    print(data_json["impedance"])
    if (int(data_json["impedance"])) in range(1,1000):
        return(data_json)

def getDatos(height):
    heightStr = height.decode("utf-8")
    heightJson = json.loads(heightStr)
    height = int(heightJson["val"])
    mac_addr = "5C:CA:D3:5B:EA:C6"  # Can be None or empty too
    callback = get_json
    send_only_stabilized_weight = False
    scale = MiScale(height,mac_addr, callback, send_only_stabilized_weight)
    return json.loads(str(scale))
    

