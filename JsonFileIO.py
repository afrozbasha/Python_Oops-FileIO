"""
    @Author: Afroz Basha
    @Date: 2021-08-26
    @Title: 2D ARRAY
"""
import sys

"""
 Read and Write operations with json file
"""

import json


class JsonFileIO(object):
    """ Read and Write operations with json file """
    def WritenJsonFile(self):
        file = open("jsonWritenFile.json", "w")
        IdCard = {
            "Name": "Afroz Basha",
            "BatchNo": "RFP-033",
            "Track Score": "4.56",
            "PhoneNum": "9533182605",
            "Address": [
                {
                    "City": "Jammalamadugu",
                    "Zip": "516434",
                    "State": "Andhra Pradesh"
                }
            ]
        }
        jsonStr = json.dumps(IdCard)
        file.write(jsonStr)
        file.close()
        pass

    def ReadJsonFile(self):
        try:
            file = open("jsonWritenFile.json", "r")
            obj = json.load(file)
            print("Name:", str(obj["Name"]))
            print("BatchNo", str(obj["BatchNo"]))
            print("Track Score:", str(obj["Track Score"]))
            print("PhoneNum", str(obj["PhoneNum"]))
            list = obj["Address"]

            for i in range(len(list)):
                print("City:", list[i].get("City"))
                print("Zip:", list[i].get("Zip"))
                print("State:", list[i].get("State"))
            file.close()
        except FileNotFoundError:
            print("File is not Found Need to create!!")
        pass


while True:
    print("\n**********************")
    print("1:File write with (.json)")
    print("2:File read with (.json")
    print("3: Exit.")
    n = int(input("Enter the choice of the file operations: "))
    x = JsonFileIO()
    switcher = {
        1: x.WritenJsonFile(),
        2: x.ReadJsonFile(),
        3: sys.exit()
    }
