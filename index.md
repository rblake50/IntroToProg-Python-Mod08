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
#### Methods

### GitHub Desktop

## Code
[Link to Python script](https://github.com/rblake50/IntroToProg-Python-Mod08/blob/main/Assigment08-Starter.py)
