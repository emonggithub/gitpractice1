class Person: # Definig Person class
  def __init__(self,name,age): # Defining the constructor
    self.name1 = name # Instance variables
    self.age1 = age
    print(f"{self.name1}: {self.age1}")

# Creating the instance/object called person1 of Person class
person1 = Person("Paul",37)
