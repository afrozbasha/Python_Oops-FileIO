"""
    @Author: Afroz Basha
    @Date: 2021-08-23
    @Title: Replace String Template
"""
import sys


class replaceString(object):
    # creating string line
    def listen(self, userName):
        try:
            if len(userName) <= 3:
                strLine = "Hello " + userName + ", How are you?"
                print(strLine)
                return strLine
                sys.exit()
            else:
                raise IOError
        except IOError:
            print("!Ensure UserName has min 3 chars")

    # replacing string
    def replace(self, user, strLine):
        strLine = strLine.replace(user, "Afroz")
        print(strLine)
        sys.exit()


# taking input passing methods via class
userName = input("Enter User Name: ")
obj = replaceString()
string = obj.listen(userName)
if string:
    obj.replace(userName, string)
