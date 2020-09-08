import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QVBoxLayout, QDialogButtonBox, QDialog, QWidget, QLineEdit, QFormLayout, QGroupBox, QLabel
from inventory import *


class Dialog(QDialog): 
    ID = 1
    # constructor 
    def __init__(self): 
        super(Dialog, self).__init__() 
  
        # setting window title 
        self.setWindowTitle("Inventory") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Add Product") 
  
        # creating spin box to select age 
        self.amountLineEdit = QLineEdit()
  
        # creating combo box to select degree 
        self.priceLineEdit = QLineEdit()
  
        # creating a line edit 
        self.nameLineEdit = QLineEdit() 

        # creating a url line edit
        self.urlLineEdit = QLineEdit() 
  
        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.addToList) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)

        
    # add to list method called when form is accepted 
    def addToList(self): 
  
        # add to inventory 
        name = self.nameLineEdit.text()
        price = self.priceLineEdit.text()
        amount = self.amountLineEdit.text()
        pageUrl = self.urlLineEdit.text()

        addToInventory(productList, self.ID, name, price, amount, pageUrl)
        self.ID += 1

        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("Name"), self.nameLineEdit) 
  
        # for price and adding input text 
        newlayout.addRow(QLabel("Price"), self.priceLineEdit) 
  
        # for amount and adding input text 
        newlayout.addRow(QLabel("Amount"), self.amountLineEdit) 

        # for url and adding input text
        newlayout.addRow(QLabel("URL"), self.urlLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()


class savingDialog(QDialog):
    def __init__(self): 
        super(savingDialog, self).__init__() 

        # setting window title 
        self.setWindowTitle("Save To File") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Saving")

        # creating file name line edit
        self.fileNameLineEdit = QLineEdit()

        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.fileSaving) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
    
    # file saving method called when form is accepted 
    def fileSaving(self): 
        fileName = self.fileNameLineEdit.text()

        # save to file 
        if len(productList) > 0:
            saveSuccess = save(productList, loadingDlg.fileLoaded, fileName)
            if saveSuccess == 0:
                loadingDlg.fileLoaded = False
                addingDlg.ID = 1
        else:
            print("\nThere is nothing to save!")
        
        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("File Name"), self.fileNameLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()

class loadingDialog(QDialog):
    fileLoaded = False
    def __init__(self): 
        super(loadingDialog, self).__init__() 

        # setting window title 
        self.setWindowTitle("Load from File") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Loading")

        # creating file name line edit
        self.fileNameLineEdit = QLineEdit()

        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.fileLoading) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
    
    # get info method called when form is accepted 
    def fileLoading(self): 
        fileName = self.fileNameLineEdit.text()

        addingDlg.ID = load(productList, fileName) + 1
        
        if addingDlg.ID != 1:
            self.fileLoaded = True
        
        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("File Name"), self.fileNameLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()

class checkingDialog(QDialog):
    fileLoaded = False
    def __init__(self): 
        super(checkingDialog, self).__init__() 

        # setting window title 
        self.setWindowTitle("Product To Check") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Checking")

        # creating product name line edit
        self.productNameLineEdit = QLineEdit()

        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.productChecking) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
    
    # product checking method called when form is accepted 
    def productChecking(self): 
        productName = self.productNameLineEdit.text()

        checkProduct(productList,productName)
        
        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("Product Name"), self.productNameLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()

class deletingDialog(QDialog):
    def __init__(self): 
        super(deletingDialog, self).__init__() 

        # setting window title 
        self.setWindowTitle("Product To Check") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Checking")

        # creating product name line edit
        self.productNameLineEdit = QLineEdit()

        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.productDeleting) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
    
    # product checking method called when form is accepted 
    def productDeleting(self): 
        productName = self.productNameLineEdit.text()

        delete(productList,productName)
        
        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("Product Name"), self.productNameLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()

class updatingDialog(QDialog): 
    # constructor 
    def __init__(self): 
        super(updatingDialog, self).__init__() 
        # setting window title 
        self.setWindowTitle("Updating Product") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Updating") 
  
        # creating spin box to select age 
        self.amountLineEdit = QLineEdit()
  
        # creating combo box to select degree 
        self.priceLineEdit = QLineEdit()
  
        # creating a line edit 
        self.nameLineEdit = QLineEdit() 

        # creating a url line edit
        self.urlLineEdit = QLineEdit() 
  
        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 

        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.updateProduct) 

        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
        
    # add to list method called when form is accepted 
    def updateProduct(self): 
        # add to inventory 
        found = False
        for item in productList:
            if item.name.lower() == productToUpdateDlg.productName.lower():
                found = True
                name = self.nameLineEdit.text()
                if name == "":
                    name = productToUpdateDlg.productName


                price = self.priceLineEdit.text()
                if price == "":
                    price = productToUpdateDlg.price


                amount = self.amountLineEdit.text()          ####Check all variables for the right one
                if amount == "":
                    amount = productToUpdateDlg.stock


                pageUrl = self.urlLineEdit.text()
                if pageUrl == "":
                    pageUrl = productToUpdateDlg.pageUrl

                item.update(name, price, amount, pageUrl)
                print("\n%s was succesfully updated." % (item.name))
                break
        if not found:
            print("\nThe item was not found.")

        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
  
        # for price and adding input text 
        newlayout.addRow(QLabel("Price"), self.priceLineEdit) 
  
        # for amount and adding input text 
        newlayout.addRow(QLabel("Amount"), self.amountLineEdit) 

        # for url and adding input text
        newlayout.addRow(QLabel("URL"), self.urlLineEdit) 
        
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.exec()

class productToUpdateDialog(QDialog):
    productName = ""
    price = ""
    stock = ""
    pageUrl = ""
    Found = False
    def __init__(self): 
        super(productToUpdateDialog, self).__init__() 

        # setting window title 
        self.setWindowTitle("Finding Product") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Updating")

        # creating product name line edit
        self.productNameLineEdit = QLineEdit()

        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.findProductToUpdate) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
    
    # product checking method called when form is accepted 
    def findProductToUpdate(self): 
        self.productName = self.productNameLineEdit.text()

        found = False
        for item in productList:
            if item.name.lower() == self.productName.lower():
                found = True

                print("\nThe item was found.")
                self.price = item.price
                self.stock = item. stock
                self.pageUrl = item.pageUrl
                updatingDlg = updatingDialog()
                updatingDlg.showBox()
                break
        if not found:
            print("\nThe item was not found.")
        
        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("Product Name"), self.productNameLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()

class usingProductDialog(QDialog): 
    # constructor 
    def __init__(self): 
        super(usingProductDialog, self).__init__() 
        # setting window title 
        self.setWindowTitle("Using Product") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Using") 
  
        # creating spin box to select age 
        self.amountToUseLineEdit = QLineEdit()
  
        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 

        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.useProduct) 

        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
        
    # add to list method called when form is accepted 
    def useProduct(self): 
        # add to inventory 
        found = False
        for item in productList:
            if item.name.lower() == productToUseDlg.productName.lower():
                found = True
                name = productToUseDlg.productName
                price = productToUseDlg.price
                amount = productToUseDlg.stock
                pageUrl = productToUseDlg.pageUrl
                amountToUse = self.amountToUseLineEdit.text()  

                item.useProduct(amountToUse)
                
                break
        if not found:
            print("\nThe item was not found.")

        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
  
        # for amount and adding input text 
        newlayout.addRow(QLabel("Amount To Use"), self.amountToUseLineEdit) 
        
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.exec()

class productToUseDialog(QDialog):
    productName = ""
    price = ""
    stock = ""
    pageUrl = ""
    def __init__(self): 
        super(productToUseDialog, self).__init__() 

        # setting window title 
        self.setWindowTitle("Finding Product") 
  
        # setting geometry to the window 
        self.setGeometry(100, 100, 300, 400) 
  
        # creating a group box 
        self.formGroupBox = QGroupBox("Updating")

        # creating product name line edit
        self.productNameLineEdit = QLineEdit()

        # calling the method that create the form 
        self.createForm() 
  
        # creating a dialog button for ok and cancel 
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel) 
  
        # adding action when form is accepted 
        self.buttonBox.accepted.connect(self.findProductToUse) 
  
        # addding action when form is rejected 
        self.buttonBox.rejected.connect(self.reject) 
  
        # creating a vertical layout 
        mainLayout = QVBoxLayout() 
  
        # adding form group box to the layout 
        mainLayout.addWidget(self.formGroupBox) 
  
        # adding button box to the layout 
        mainLayout.addWidget(self.buttonBox) 
  
        # setting lay out 
        self.setLayout(mainLayout)
    
    # product checking method called when form is accepted 
    def findProductToUse(self): 
        self.productName = self.productNameLineEdit.text()

        found = False
        for item in productList:
            if item.name.lower() == self.productName.lower():
                found = True

                print("\nThe item was found.")
                self.price = item.price
                self.stock = item. stock
                self.pageUrl = item.pageUrl
                usingProductDlg = usingProductDialog()
                usingProductDlg.showBox()
                break
        if not found:
            print("\nThe item was not found.")
        
        # closing the window 
        self.close() 
  
    # creat form method 
    def createForm(self): 
  
        # creating a form layout 
        newlayout = QFormLayout() 
  
        # adding rows 
        # for name and adding input text 
        newlayout.addRow(QLabel("Product Name"), self.productNameLineEdit) 
  
        # setting layout 
        self.formGroupBox.setLayout(newlayout) 
    
    def showBox(self):
        self.show()



def printInventory():
    printStockList(productList)

def clearInventory():
    productList.clear()
    addingDlg.ID = 1
    print("\nInventory list was cleared!")

    


productList = []

#Create appplication in memory
app = QApplication(sys.argv)

#Create the window in memory
window = QWidget()

#Set Window title
window.setWindowTitle('Inventory')

#Build layout in grid style in memory
layout = QGridLayout()

#Add the buttons to the layout in memory and connect them to dialog boxes
button1 = QPushButton('Add Product')
addingDlg = Dialog()
button1.clicked.connect(addingDlg.showBox)


button2 = QPushButton('Delete Product')
deletingDlg = deletingDialog()
button2.clicked.connect(deletingDlg.showBox)

button3 = QPushButton('Check Inventory')
checkingDlg = checkingDialog()
button3.clicked.connect(checkingDlg.showBox)

button4 = QPushButton('Use Inventory')
productToUseDlg = productToUseDialog()
button4.clicked.connect(productToUseDlg.showBox)

button5 = QPushButton('Update Item Data')
productToUpdateDlg = productToUpdateDialog()
button5.clicked.connect(productToUpdateDlg.showBox)

button6 = QPushButton('Clear Inventory List')
button6.clicked.connect(clearInventory)

button7 = QPushButton('Print Inventory List')
button7.clicked.connect(printInventory)

button8 = QPushButton('Save')
savingDlg = savingDialog()
button8.clicked.connect(savingDlg.showBox)

button9 = QPushButton('Load')
loadingDlg = loadingDialog()
button9.clicked.connect(loadingDlg.showBox)

layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 0, 1)
layout.addWidget(button3, 0, 2)
layout.addWidget(button4, 1, 0)
layout.addWidget(button5, 1, 1)
layout.addWidget(button6, 1, 2)
layout.addWidget(button7, 2, 0)
layout.addWidget(button8, 2, 1)
layout.addWidget(button9, 2, 2)

#Set the layout to the layout built in memory
window.setLayout(layout)

#Show the layout built in memory
window.show()

#Execute app
sys.exit(app.exec_())