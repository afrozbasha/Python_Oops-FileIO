"""
    @Author: Afroz Basha
    @Date: 2021-08-26
    @Title: 2D ARRAY
"""
import sys
import csv

"""
 Read and Write operations with CSV file
"""


class CSVFileIO(object):
    """Read and Write operations with CSV file"""

    def readCSVFile(self):
        try:
            with open("AddressBook.csv", "r") as file:
                reader = csv.reader(file, delimiter=",")
                header = next(reader)
                for row in reader:
                    firstName = row[0]
                    lastName = row[1]
                    address = row[2]
                    city = row[3]
                    state = row[4]
                    zip = row[5]
                    phoneNum = row[6]
                    email = row[7]
                    print("firstName: ", firstName)
                    print("lastName: ", lastName)
                    print("address: ", address)
                    print("city: ", city)
                    print("state: ", state)
                    print("zip: ", zip)
                    print("phoneNum: ", phoneNum)
                    print("email: ", email)
        except FileNotFoundError:
            print("File is not Found Need to create!!")
        pass

    def writeCSVFile(self):
        """writing to csv file"""
        fields = ["firstName", "lastName", "address", "city", "state", "zip",
                  "phoneNum", "email"]
        rows = [["Afroz", "Basha", "kapu", "jammalamadugu", "Andhra Pradesh",
                "51643", "9533182605", "iafrozbasha@gmail.com"]]
        file = "Book.csv"

        # writing to csv file
        with open(file, "w") as csvFile:
            csvwriter = csv.writer(csvFile)

            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerows(rows)
        pass


while True:
    print("\n**********************")
    print("1:File write with (.CSV)")
    print("2:File read with (.CSV")
    print("3: Exit.")
    x = CSVFileIO()
    n = int(input("Enter the choice of the file operations: "))
    switcher = {
        1: x.readCSVFile(),
        2: x.writeCSVFile(),
        3: sys.exit()
    }
