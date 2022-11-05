# class Bobi:
#     def __init__(self ,age,gerder):
#         self.age = age
#         self.gerder = gerder
#     def __str__(self):
#         return f'{self.age} {self.gerder} '

# p = Bobi(52, 'boooob battle')
# print(p)


class Monkey:
    max_age = 44
    loves_bananas = True

    def climb(self):
        print('i like to eat banana')

monkey = Monkey()
print(monkey.max_age)
print(monkey.loves_bananas)
        
a = Monkey()
a.climb()

b = Monkey()
b.climb()


# class Brand:
#    def __init__(self , name , age , gender) -> None:
#       self.name = name
#       self.age = age
#       self.gender = gender
   
#    def calculate_age(self , kub):
#       self.kub = kub
      
#    def __str__(self) -> str:
#       if self.kub :
#          return f'Firm: {self.name}\nData: {self.age + self.kub} years\nSize: {self.gender}'
#       else :
#          return f'Firm: {self.name}\nData: {self.age} лет\nSize {self.gender}'
   
# street = Brand('Nike' , 46 , '36 - 48')
# street.calculate_age(12)
# print(street)