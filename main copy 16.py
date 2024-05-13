# b = {
#     "car" : "Toyota",
#     "model" :"camry",
#     "imeges" : ['https://cam50-imege','https://cam75-imege'],
#     "price" : 25000000,
#     "is_published" : True
#     }

# a = {
#     "car" : "Toyota",
#     "model" :"camry",
#     "imege" : ['https://cam50-imege'],
#     }


# list_1 = [
#     {
#         "name" :"Kanat",
#         "last_name":"Erbolov",
#         "age": 43
#     },
#     {
#         "name": "Miras",
#         "last_name": "Miko",
#         "age": 18
#     },
#     {
#         "name": "Agibay",
#         "last_name": "Zhandosov",
#         "age": 99
#     }
# ]
# t=0
# for n in list_1:
#     t += n["age"]

# n=len(list_1)
# c = t/n
# print(c)


# class A: # class esimi ,atu
#     attr = "Hello World" # класс атрибуты
#     def hello(self): 
#      print (self .attr)

# objt = A()
# hello = objt.hello()
# print(hello) 


# class Person:
#    def __init__(self,name,age, firstname=""):
#       self.name = name
#       self.firstname = firstname
#       self.age = age 
#    def my_method(self):
#       if self.firstname :
#          print ("My name fastname age" ,   self.name  ,   self.firstname ,   self.age )
#       else:
#           print("My name fastname age " ,   self.name ,   self.age)  
# p1 = Person("Yerkebulan ","17","Akhmet " )
# p1.my_method() 
# p2 = Person("Yerkebulan",  "17")
# p2.my_method()


class Cars:
   def __init__(self,car_name,car_model,car_year) :
      self.car_name = car_name
      self.car_model = car_model
      self.car_year = car_year
   def cars(self):
      if self.car_model:
         print (self.car_name,self.car_model,self.car_year) 
      else:
         print (self.car_name,self.car_year) 
car1 = Cars("toyota","camry","2024")         
car1.cars()
