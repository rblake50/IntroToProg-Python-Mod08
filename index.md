# Module 08 Webpage

[Link to repository](https://github.com/rblake50/IntroToProg-Python-Mod08)
<br>[Link to page index](https://github.com/rblake50/IntroToProg-Python-Mod08/tree/gh-pages)

## Introduction
This document investigates objects within a class and how they can be initiated, constructed, and accessed. Objects within classes offer a number of advantages compared to simple variables such as organized error handling and function definition. This document will discuss the basics for objects in classes, the fundamentals of objects, and code management through GitHub desktop. The script example will illustrate all learnings and be published to GitHub through the desktop application.

## Topics
- Class objects
- Object fundamentals
- GitHub desktop

## Summary 
### Objects in Classes
A general outline for objects in a class is written below:
```python
class Product:
  # Fields
  # Constructors
    # Attributes
  # Properties
  # Methods
```
Following this outline takes a linear approach to object initiation that can be simply understood by other programmers. Each topic will be explored in the next section.

### Object Fundamentals
#### Fields
Fields comprise the data for an object within a class. These can be thought of as characteristics that would apply to any object. For example, a Product might be describe by a product name and a product price. Thus, `product_name` and `product_price` could be suitable fields for an object called `Product`.
```python
class Product:
  product_name = ""
  product_price = 0.0
```
These fields act as placeholders for values that can be initiated and changed through constructors and properties as mentioned in the next sections.
#### Constructors
Constructors are built-in methods to Python that help define an object when it is initiated. Two useful constructor methods are `__init__(self)` and `__str(self)__`. Respectively, these methods define what happens right when an object is initialized and what happens when an object is printed as text. Note that all constructors must be written within a class.

The initialization method can give default values for specified attributes. The example below creates a product with a blank product name (initially) and a price as a zero float.
```python
def __init__(self):
  print("A new product has been created!")
  
  # Attributes
  self.product_name = ""
  self.product_price = 0.0
```
Attributes can also be made "private" such that the attribute cannot be directly accessed through the class. Private attributes are created with two underscores as a prefix to the attribute name. From the above example, the second attribute could be made private by writing `self.__product_price = 0.0`. More discussion on private attributes can be found in Chapter 8 of the textbook.

The string method constructs how Python prints an object. Without a string constructor, the text may not be intuitive to a user. The example below concatenates object attributes into a coherent message when the object is directly printed.
```python
def __str__(self):
  tmp = "name: " + self.product_name + ", price: $.2f" % self.product_price
  return tmp
```
#### Properties
Properties act as functions to manage attributes. For example, properties can ensure attribute definition is proper or format attribute data.

The nomenclature for properties can be confusing at first glance. Conversationally, properties can be thought of as "getters" or "setters." Getters retrieve attributes when commanded. Setters assign values for attributes when commanded. The example below outlines the basic syntax for getters and setters.

```python
@property # Getter
def product_price(self):
  return self._product_price
  
@product_price.setter # Setter
def product_price(self,price):
  try:
    self._product_price = float(price)
  except ValueError:
    print("D'oh! Price must be a number. Try again.")
```
As mentioned, the syntax is critical, and the variable name should be consistent with the attribute from earlier. The getter retrieves the object's (self) attribute value. The setter assigns a value to the attribute and handles errors in the process. Though tedious, it is a best practice to write a getter and setter property for each attribute within a class.

#### Methods
Methods are more or less functions within a class that do not manage attributes. Consider another class example to illustrate a simple method.

```python
class FileProcessor:
  # Save data to a pickled file
  @staticmethod
  def save_data_to_file(file_name, list_of_product_objects):
    with open(file_name, 'wb'):
      pickle.dump(list_of_product_objects, file)
    print("File successfully pickled to " + file_name)
```

### GitHub Desktop
GitHub Desktop offers another avenue for managing files and committing changes on GitHub in addition to the web browser. GitHub Desktop can be installed from the [GitHub website](https://desktop.github.com/).

Some of the key benefits of GitHub Desktop include:
- File management using Windows explorer
- Clean user interface
- Collaboration

Though not explored in this module, the multi-user collaboration tools offer a way for multiple developers to work on the same files with clear change history.

## Assignment Description
This program allows a user to read list data from a pickled file and read or add data to the list. Then, the user can exit the program and save the data back to the pickled file. The data being stored is Product information containing the name and price of the Product. The Product is managed as a Python object through class properties.

The pseudocode provided is:
```python
# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
```

## Code
[Link to Python script](https://github.com/rblake50/IntroToProg-Python-Mod08/blob/main/Assigment08-Starter.py)
