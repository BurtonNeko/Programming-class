# Create a Character class with the following fields:
# (1) name - the name of the character
# (2) health - the health of the character, with value between 0 to 100
# (3) attack_power - the attack power of the character, with value between 10 to 100
class Character:

    def __init__(self, name, health, attack_power):
        if not (0 <= health <= 100):
            raise ValueError("Health must be between 0 and 100.")
            if not (10 <= attack_power <= 100):
                raise ValueError("Attack power must be between 10 and 100.")
    
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
# When an instance of Character is created, the value to all three fields are required.
# Once completed, create two instances of Character to two of your most favourite game characters.
# Two favorite game characters
char1 = Character("Elden King", 95, 80)
char2 = Character("Lara Croft", 85, 70)

# Display their details
char1.display_details()
print()  # Just for spacing
char2.display_details()

# Then, write code to print the details of each character.
default_char = Character("Default Hero")
default_char.display_details()




# How would you change the __init__ function so that by default the health is 100
# and attack_power is 10.

    
