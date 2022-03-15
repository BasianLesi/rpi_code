from Naked.toolshed.shell import execute_js, muterun_js
import json


def updateVoltage(v):
    a_file = open("config.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["voltage"] = round(v)

    a_file = open("config.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


v = 5;

for i in range(5):
    updateVoltage(v)
    v += 3
    success = execute_js('index.js')

