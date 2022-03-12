# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# FSharif,3.6.2022,Created started script
# FSharif,3.6.2022,Added pseudo-code to start assignment 8
# <Fatima Sharif>,<2.6.2022>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    # --Fields--
    strProductName = ""
    fltProductPrice = ""

    # --Constructor--
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- properties --
    # product name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value: str):
        self.__product_name = value

    # product_price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Prices must be numbers")

    # -- methods --
    def to_string(self):
        """ alias of __str__(), converts product data to string """
        return self.__str__()

    def __str__(self):
        """ Converts product data to string """
        return self.product_name + "," + str(self.product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:

    # TODO: Add Code to process data from a file
    @staticmethod
    def save_data_to_file(file_name: str, list_of_product_objects: list):
        success_status = False
        try:
            file = open(file_name, "w")
            for product in list_of_product_objects:
                file.write(product.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status
    # TODO: Add Code to process data to a file
    @staticmethod
    def read_data_from_file(file_name: str):
        list_of_product_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                data = line.split(",")
                row = Product(data[0], data[1])
                list_of_product_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_product_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #

class IO:  # TODO: Add docstring
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user """
        print('''
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Save Data to File
    4) Exit Program
    ''')

    print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():

        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice
    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_list_items(list_of_rows: list):

        print("******* The current items products are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Add code to get product data from user
    @staticmethod
    def input_product_data():

        try:
            name = str(input("What is the product name? - ").strip())
            price = float(input("What is the price? - ").strip())
            print()  # Add an extra line for looks
            p = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return p
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program



# Main Body of Script  ---------------------------------------------------- #
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
    while True:
        IO.print_menu_items() # Show user a menu of options
        strChoice = IO.input_menu_choice() # Get user's menu option choice
        if strChoice.strip() == '1':
            IO.print_current_list_items(lstOfProductObjects) # Show user current data in the list of product objects
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_product_data())
            continue
        elif strChoice.strip() == '3':
            # let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue
        elif strChoice.strip() == '4':
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')