# Character Factory Design Pattern in Python

This repository demonstrates the implementation of the **Prototype Design Pattern** in Python. The `CharacterFactory` class is used to create new characters based on a prototype, allowing you to clone and customize characters easily. This approach allows for efficient creation of characters with only the required attributes being modified.

## Overview

The prototype design pattern is a creational design pattern used to clone existing objects to create new instances. In this project, the `CharacterFactory` class provides methods for creating characters with modified attributes by cloning a default prototype character.

## Project Structure

- `Character.py`: Defines the `Character` class, which represents a character with attributes such as `name`, `health`, `attack_power`, and `level`.
- `CharacterFactory.py`: Defines the `CharacterFactory` class, which creates and clones characters using a prototype.

## Classes

### `Character`
The `Character` class defines the attributes of a character:
- `name`: The name of the character.
- `health`: The health of the character.
- `attack_power`: The attack power of the character.
- `level`: The level of the character.

It also includes the `clone` method that uses Python’s `copy.deepcopy` to create a clone of the character.

### `CharacterFactory`
The `CharacterFactory` class manages the prototype character and contains methods for creating new characters by cloning the prototype and modifying specific attributes:
- `create_character_with_new_name(name)`: Clones the prototype character and assigns a new name.
- `create_character_with_new_level(level)`: Clones the prototype character and assigns a new level.
- `create_character_with_new_attack_power(attack_power)`: Clones the prototype character and assigns a new attack power.

## Example Usage

```python
from CharacterFactory import CharacterFactory

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
```
Expected Output:
```yaml
Warrior: Warrior, Level: 1
Mage: Mage, Level: 1
Knight: DefaultName, Level: 5
```
