from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name) #название продукта
        self.weight = float(weight) #общий вес товара
        self.category = str(category) #категория товара

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        prod_str = file.read()
        file.close()
        return prod_str

    def add(self, *products):
        existing_products = self.get_products()
        for i in products:
            if i.name in existing_products:
                print(f'Продукт {i.name} уже есть в магазине')
            else :
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())