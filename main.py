import copy

class Character:
    def __init__(self, name, health, attack_power, level):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.level = level

    def clone(self):
        return copy.deepcopy(self)  # Use deepcopy to clone the object

class CharacterFactory:
    def __init__(self):
        # Constructor to create a prototype character (default character)
        self.prototype_character = Character("DefaultName", 100, 50, 1)  # Default prototype character

    def create_character_with_new_name(self, name):
        cloned_character = self.prototype_character.clone()
        cloned_character.name = name
        return cloned_character

    def create_character_with_new_level(self, level):
        cloned_character = self.prototype_character.clone()
        cloned_character.level = level
        return cloned_character

    def create_character_with_new_attack_power(self, attack_power):
        cloned_character = self.prototype_character.clone()
        cloned_character.attack_power = attack_power
        return cloned_character

# Create an instance of the CharacterFactory
factory = CharacterFactory()

# Create characters with new names
warrior = factory.create_character_with_new_name("Warrior")
mage = factory.create_character_with_new_name("Mage")

# Create a character with a new level
knight = factory.create_character_with_new_level(5)

# Optional: Print the character details to verify
print(f"Warrior: {warrior.name}, Level: {warrior.level}")
print(f"Mage: {mage.name}, Level: {mage.level}")
print(f"Knight: {knight.name}, Level: {knight.level}")
