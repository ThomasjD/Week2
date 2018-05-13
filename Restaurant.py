#Make a class called Restaurant. The __init__ method for Restaurant should store two attributes. a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restuarant() that prints a message indicating that the restaurant is open.

#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

Class Restaurant:
  def __init__(self, restaurant_name, cuisine_type)
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurante(self)
    print (self.restaurant_name)
    print(self.cuisine_type)

Frenchy = Restaurant('Frenchy', 'fried chicken')

#creating object/instance of store Class
Frenchy.describe_restaurant()
print (Frenchy.restaurant_name)
print (Frenchy.cuisine_type)
