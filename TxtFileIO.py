"""
    @Author: Afroz Basha
    @Date: 2021-08-26
    @Title: 2D ARRAY
"""
import sys

"""
 Read and Write operations with txt file
"""


class TxtFileIO(object):
    """ Read and Write operations with txt file """
    @staticmethod
    def txtFileWrite():
        file = open("txtWritenFile.txt", "w")
        file.write("This Txt file is writen by Python Program")
        file.close()
        pass

    def txtFileWriteAppend(self):
        file = open("txtWritenFile.txt", "a")
        file.write("\nThis program writen by Afrozbasha")
        file.close()
        pass

    @classmethod
    def txtFileRead(cls):
        try:
            file = open("txtWritenFile.txt", "r")
            txt = file.read()
            print('"', txt, '"')
            file.close()
        except FileNotFoundError:
            print("File is not Found Need to create!!")
        pass

    def readLinebyLine(self):
        try:
            file = open("txtWritenFile.txt", "r")
            txt = file.readlines()
            print(txt)
            file.close()
        except FileNotFoundError:
            print("File is not Found Need to create!!")
        pass


while True:
    print("\n**********************")
    print("1:File write with (.txt)")
    print("2:File read with (.txt)")
    print("3:File read Line by Line with (.txt)")
    print("4:File write with Append Mode (.txt)")
    print("5: Exit.")
    n = int(input("Enter the choice of the file operations: "))
    x = TxtFileIO()
    switcher = {
        1: x.txtFileWrite(),
        2: x.txtFileRead(),
        3: x.readLinebyLine(),
        4: x.txtFileWriteAppend(),
        5: sys.exit()
    }
