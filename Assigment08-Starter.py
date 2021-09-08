# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# rblake50, 09.04.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
# DESCRIPTION
# This program allows a user to read list data from a pickled file and
# read or add data to the list. Then, the user can exit the program and
# save the data back to the pickled file. The data being stored is Product
# information containing the name and price of the Product. The Product is
# managed as a Python object through class properties.
# ------------------------------------------------------------------------ #
# ASSUMPTIONS
# The user is reading from and writing to a pickled file (such as .dat)
# that is properly organized with Product objects

import pickle
from datetime import datetime

# Data -------------------------------------------------------------------- #
strFileName = 'products.dat'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        rblake50,09.04.2021,Modified code to complete assignment 8
    """

    # Fields
    product_name = ""
    product_price = 0.0

    # Constructors
    def __init__(self):
        print("A new product has been added!")

        # Attributes
        self.product_name = ""
        self.product_price = 0.0

    def __str__(self):
        tmp = "name: " + self._product_name + ", price: $%.2f" % self._product_price
        return tmp

    # Properties
    @property # Getter
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self,name):
        self._product_name = name

    @property # Getter
    def product_price(self):
        return self._product_price

    @product_price.setter
    def product_price(self,price):
        try:
            self._product_price = float(price)
        except ValueError:
            print("D'oh! Price must be a number. Try again.")

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    properties:
        N/A
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        :param file_name (string) name of file to save
        :param list_of_product_objects (list) of product objects

        read_data_from_file(file_name): -> (a list of product objects)
        :param file_name (string) name of file to read
        :return list of product objects

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        rblake50,09.04.2021,Modified code to complete assignment 8
    """

    # Save data to a pickled file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):

        with open(file_name, 'wb') as file:
            pickle.dump(list_of_product_objects, file)

        print("File successfully pickled to " + file_name)

    # Save data to .txt file
    @staticmethod
    def save_data_to_txt(file_name, list_of_product_objects):

        file_prefix = file_name.split(".")[0]
        file_to_save = file_prefix + ".txt"

        with open(file_to_save, 'w') as file:

            file.write(datetime.now().strftime("%m/%d/%y, %H:%M:%S\n======\n"))
            for item in list_of_product_objects:
                file.write(item.__str__() + "\n")

        print("Text file successfully written to " + file_to_save)

    # Read data from a pickled file
    @staticmethod
    def read_data_from_file(file_name):

        lstData = [] # Initiate as list

        try:
            with open(file_name, 'rb') as fileIncoming:
                lstData = pickle.load(fileIncoming)

        except FileNotFoundError: # File does not exist in immediate directory
            print("The file " + file_name + " does not exist! Add data and save to create file.")

        except EOFError: # File exists in immediate directory but has no information
            input("The file has no content! Please add data.")

        return lstData

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Manages user input and file output

    properties:
    methods:
        show_menu()
            1. Show user current data in the list of product objects
            2. Let user add data to the list of product objects
            3. let user save current data to file and exit program

        return_to_menu()

        get_choice()
        :return string of user choice

        show_data(file_name)
        :param list_of_product_objects (list) of product objects to show

        get_data()
        :return Product object with name and price of product

    changelog: (When,Who,What)
        rblake50,09.04.2021,Modified code to complete assignment 8
    """
    # Show menu to user
    @staticmethod
    def show_menu():
        strMenu = "=== MENU ===\n1. Show current data\n2. Add product\n3. Save and exit"
        print(strMenu)

    # Show prompt to return to menu
    @staticmethod
    def return_to_menu():
        input("Press ENTER to return to menu.")

    # Get user's choice
    @staticmethod
    def get_choice():
        strChoice = input("What is your choice? ")
        return strChoice

    # Show the current data from the file to user
    @staticmethod
    def show_data(list_of_product_objects):

        if len(list_of_product_objects) != 0:
            try:
                print("Here is your list of items:")
                for item in list_of_product_objects:
                    print(item)

            except TypeError:
                input("List is the wrong type! Please add data.")

        else:
            print("The list is empty. Please add items.")

    # Get product data from user
    @staticmethod
    def get_data():

        try:
            name = input("What is the product name? ")
            price = float(input("What is the product price? "))

            prod = Product()
            prod.product_name = name
            prod.product_price = price

            return prod

        except ValueError:
            print("D'oh! Price must be a number. Try again.")

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

# Show data from loaded file
IO.show_data(lstOfProductObjects)

while True:

    # Show user a menu of options
    IO.show_menu()

    # Get user's menu option choice
    choice = IO.get_choice()

    # 1. Show user current data in the list of product objects
    if choice == "1":

        IO.show_data(lstOfProductObjects)

        IO.return_to_menu()

    # 2. Let user add data to the list of product objects
    elif choice == "2":
        print("You chose to add data to the list.")

        # Get data for new Product from user
        product = IO.get_data()
        if product is not None: # get_data() will return None for invalid entry
            lstOfProductObjects.append(product)

        # Prompt return to menu
        IO.return_to_menu()

    # 3. let user save current data to file and exit program
    elif choice == "3":

        print("You chose to save and exit.")

        # Prompt user for a text file copy of the data
        print("Do you want to export a .txt file? [y]es or [n]o.")
        choice = IO.get_choice().lower()

        # User wants to save text file
        if choice == "y" or choice == "yes":

            # Save data to pickled file and text file with same file name (less extension)
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            FileProcessor.save_data_to_txt(strFileName, lstOfProductObjects)
            break

        # User does not want to save text file
        elif choice == "n" or choice == "no":

            # Save data to pickled file but *NOT* to text file
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("File *NOT* written to text file.")
            input("Good-bye!")
            break

        # Invalid entry
        else:

            print("Invalid selection! Data will not be saved.")
            IO.return_to_menu()

    # Invalid choice
    else:
        print("D'oh! Your choice is invalid.")
        IO.return_to_menu()