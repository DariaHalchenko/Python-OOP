"""Zoo."""


class Animal:
    """Animal class."""

    def __init__(self, name: str, specie: str, age: int):
        """
        Class constructor.

        Each animal has a name and a specie.
        :param name: animal name
        :param specie: animal specie
        """
        self.name = name
        self.specie = specie
        self.age = age


class Zoo:
    """Zoo class."""

    def __init__(self, name: str, max_number_of_animals: int):
        """
        Class constructor.

        Each zoo has a name and max number of animals the zoo can have.
        There also should be an overview of all animals present in the zoo.

        :param name: zoo name
        :param max_number_of_animals: how many animals can be in the zoo
        """
        self.name = name
        self.max_number_of_animals = max_number_of_animals
        self.animals = []

    def can_add_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be added to the zoo.

        Animal can be added to the zoo if:
        1. Adding a new animal does not exceed zoo's max number of animals.
        2. Same Animal object is not present in the zoo.
        3. Animal with same name and specie is not yet present in the zoo.
        :param animal: animal who is checked
        :return: bool describing whether the animal can be added to the zoo or not
        """
        if animal in self.animals:
            return False
        for existing_animal in self.animals:
            if existing_animal.name == animal.name and existing_animal.specie == animal.specie:
                return False
        return len(self.animals) < self.max_number_of_animals

    def add_animal(self, animal: Animal):
        """
        Add animal to the zoo if possible.

        :param animal: animal who is going to be added to the zoo
        Function does not return anything
        """
        if self.can_add_animal(animal):
            self.animals.append(animal)

    def can_remove_animal(self, animal: Animal) -> bool:
        """
        Check if animal can be removed from the zoo.

        Animal can be removed from the zoo if animal is present in the zoo.

        :param animal: animal who is checked
        :return: bool describing whether animal can be removed from the zoo or not.
        """
        return animal in self.animals

    def remove_animal(self, animal: Animal):
        """
        Remove animal from the zoo if possible.

        :param animal: animal who is going to be removed from the zoo.
        Function does not return anything
        """
        if self.can_remove_animal(animal):
            self.animals.remove(animal)

    def get_all_animals(self):
        """
        Return a list with all the animals in the zoo.

        :return: list of Animal objects
        """
        return self.animals

    def get_animals_by_age(self):
        """
        Return a list of animals sorted by age (from younger to older).

        :return: list of Animal objects sorted by age
        """
        return sorted(self.animals, key=lambda x: x.age)

    def get_animals_sorted_alphabetically(self):
        """
        Return a list of animals sorted (by name) alphabetically.

        :return: list of Animal objects sorted by name alphabetically
        """
        return sorted(self.animals, key=lambda x: x.name)

if __name__ == "__main__":
    # Loomade loomine
    lõvi = Animal("Griša", "lõvi", 6)
    elevant = Animal("Lisa", "elevant", 2)
    laama = Animal("Alice", "laama", 5)
    ahv=Animal("Tolik", "ahv", 1)
    krokodill=Animal("Aleksei", "krokodill", 8)
    zoo = Zoo("Tallinn Zoo", 10)
    zoo.add_animal(lõvi)
    zoo.add_animal(elevant)
    zoo.add_animal(laama)
    zoo.add_animal(ahv)
    zoo.add_animal(krokodill) 
    all_animals = zoo.get_all_animals()
    print(all_animals)
    animals_by_age = zoo.get_animals_by_age()
    print(animals_by_age)
    animals_sorted_alphabetically = zoo.get_animals_sorted_alphabetically()
    print(animals_sorted_alphabetically)
