class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'{self.name}, {self.age}'

    def birthday(self):
        self.age += 1

class Dog(Animal):

    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_domestic: bool=True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog: {self.color}, {self.breed}, домашняя'
        return f'Dog: {self.color}, {self.breed}, дворняга'


class Kotopes(Animal):
    def __init__(self, name: str,
                 age: int,
                 number_heads: int = 2) -> None:
        super().__init__(name, age)

        self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes: number_heads: {self.__number_heads}, {self.age} '


class Fish(Animal):

    def __init__(self,
                 name,
                 age,
                 aqua,
                 size):
        super().__init__(name, age)

        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'Fish: морская, {self.size}'
        else:
            return f'Fish: пресноводная, {self.size}'


class Factory:
    def create_animal(self, animal_type, *args):
        if animal_type == 'Dog':
            return Dog(*args)
        elif animal_type == 'Kotopes':
            return Kotopes(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        else:
            raise ValueError("Invalid animal type")



if __name__ == '__main__':
    f = Factory()
    d1 = f.create_animal('Dog', 'Sharik', 2, 'black', 'bulldog', True)
    print(d1)
    f1 = f.create_animal('Fish', 'Dori', 1, True, 0.5)
    print(f1)
    kp1 = f.create_animal('Kotopes', 'Marti', 55)
    print(kp1)
    kp1.birthday()
    print(kp1)