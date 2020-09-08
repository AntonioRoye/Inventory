import os
from os import path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Product(object):
    inStock = True

    def __init__(self, ID, name, price, stock, pageUrl):
        self.ID = ID
        self.name = name
        self.price = price
        self.stock = stock
        self.pageUrl = pageUrl

    def useProduct(self, amountToUse):
        print("\nStock available: %.2f" % (float(self.stock)))
        print("\nUsing...")
        if float(amountToUse) > float(self.stock):
            print("\nThere isn't enough stock available")
        else:
            self.stock = float(self.stock) - float(amountToUse)
            print("\nStock left: %.2f" % (float(self.stock)))
            if float(self.stock) == 0:
                sendEmail(self)
                self.inStock = False
                print("\nThe item is now unavailable. An RA has been notified.")

    def update(self, name, price, stock, pageUrl):
        
            try:
                self.price = price
            
            except ValueError:
                print("That was an invalid price value")
 
            try:
                self.stock = stock

            except ValueError:
                print("That was an invalid amount value")

            try:
                self.pageUrl = pageUrl
    
            except ValueError:
                print("That was an invalid URL value")

    def displayInfo(self):
        print("\nName: %s" % (self.name))
        print("Price: $%.2f" % (float(self.price)))
        print("Stock: %.2f" % (float(self.stock)))
        print("URL: %s" % (self.pageUrl))


def menu():
    print("\n************* Menu *************")
    print(
        "\n(0) Exit. \
        \n(1) Add a new product.\
        \n(2) Delete a product.\
        \n(3) Check stock.\
        \n(4) Use stock.\
        \n(5) Update item data.\
        \n(6) Clear stock list.\
        \n(7) Print stock list.\
        \n(8) Save to file.\
        \n(9) Load from file.\n"
    )
    print("********************************\n")


def printStockList(lst):
    idStr = "ID"
    nameStr = "Name"
    priceStr = "Price"
    stockStr = "Stock"
    urlStr = "URL"

    print()
    print(idStr.center(5, " "), "|", nameStr.center(20, " "), "|", priceStr.center(
        10, " "), "|", stockStr.center(5, " "), "|", urlStr.center(20, " "))
    print("----------------------------------------------------------------------")
    for item in lst:
        print(str(item.ID).center(5, " "), "|", str(item.name).center(20, " "), "|", str("$" + item.price).center(
            10, " "), "|", str(item.stock).center(5, " "), "|", str(item.pageUrl).center(20, " "))


def addToInventory(lst, ID, name, price, stock, pageUrl):
    reagent = Product(ID, name, price, stock, pageUrl)
    print("\n%s was succesfully added." % (reagent.name))
    lst.append(reagent)



def delete(lst, productName):
    found = False
    for item in lst:
        if item.name.lower() == productName.lower():
            found = True
            lst.remove(item)
            print("\n%s was succesfully deleted." % (item.name))
            break
    if not found:
        print("\nThe item was not found.")


def checkProduct(lst, productName):
    found = False
    for item in lst:
        if item.name.lower() == productName.lower():
            found = True
            item.displayInfo()
            break
    if not found:
        print("\nThe item was not found.")

def sendEmail(self):
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login('antonio_@live.ca', 'ANT0nio1!1!2299')

    msg = MIMEMultipart()     
    message = "The item \"%s\" is out of stock. It costs $%.2f and was bought from %s" % (self.name, float(self.price), self.pageUrl)
    
    msg['From']= 'antonio_@live.ca'
    msg['To']= 'antonio_@live.ca'
    msg['Subject']= "OUT OF STOCK"
        
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
        
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    s.quit()


def save(lst, fileLoaded, fileName):

    if path.exists(fileName):

        filesize = os.path.getsize(fileName)

        if filesize == 0:
            while True:
                try:
                    with open(fileName, 'w') as f:
                        print("\nWriting to file...")
                        for item in lst:
                            f.write(str(item.ID) + " " + item.name + " " + str(item.price) +
                                    " " + str(item.stock) + " " + item.pageUrl + "\n")
                        print("\nItems were successfully saved to file.\n")
                    lst.clear()
                    return 0
            
                except:
                    print('\nItems were not saved to file.')
                    return 1
                
        else:
            if fileLoaded:
                while True:
                    try:
                        with open(fileName, 'r+') as f:
                            print("\nWriting to file...")

                            f.seek(0, 0)
                            f.truncate()

                            for item in lst:
                                f.write(str(item.ID) + " " + item.name + " " + str(item.price) +
                                        " " + str(item.stock) + " " + item.pageUrl + "\n")
                            print("\nItems were successfully saved to file.")
                        lst.clear()
                        return 0
                    
                    except:
                        print('\nItems were not saved to file.')
                        return 1
                    
            else:
                while True:
                    try:
                        with open(fileName, 'a') as f:
                            print("\nWriting to file...")

                            IDCurrent = 1
                            IDPrevious = 0
                            for line in open(fileName):
                                tempList = line.split()
                                IDPrevious = IDCurrent
                                IDCurrent = tempList[0]

                            IDCurrent = int(IDCurrent)

                            for item in lst:
                                f.write(str(item.ID + IDCurrent) + " " + item.name + " " + str(item.price) +
                                        " " + str(item.stock) + " " + item.pageUrl + "\n")
                            print("\nItems were successfully saved to file.")
                        lst.clear()
                        return 0
                    
                    except:
                        print('\nItems were not saved to this file.')
                        return 1
                
    else:
        while True:
            try:
                with open(fileName, 'w') as f:
                    print("\nWriting to file...")
                    for item in lst:
                        f.write(str(item.ID) + " " + item.name + " " + str(item.price) +
                                " " + str(item.stock) + " " + item.pageUrl + "\n")
                    print("\nItems were successfully saved to file.")
                lst.clear()
                return 0
                
            except:
                print('\nItems were not saved to file.')
                return 1
            


def load(lst, fileName):
    if path.exists(fileName):
        lst.clear()
        while True:
            try:
                with open(fileName, 'r') as f:
                    print("\nReading file...")
                    for line in f:
                        tempList = line.split()
                        reagent = Product(
                            tempList[0], tempList[1], tempList[2], tempList[3], tempList[4])
                        ID = tempList[0]
                        lst.append(reagent)
                    print("\nItems were successfully loaded from the file.")
                    return int(ID)
            except TypeError:
                print('\nItems were not loaded from the file.')
                break
    else:
        print("\nThis file does not exist!")
        return 0
