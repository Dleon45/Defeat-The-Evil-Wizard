import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(15, 25)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print(f"{self.name} uses 'Berserker Strike'!")
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage with Berserker Strike!")

# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print(f"{self.name} casts 'Fireball'!")
        damage = self.attack_power + random.randint(5, 15)
        opponent.health -= damage
        print(f"{self.name} deals {damage} damage with Fireball!")

# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)

    def special_ability(self, opponent):
        print(f"{self.name} uses 'Quick Shot'!")
        damage1 = random.randint(10, 20)
        damage2 = random.randint(10, 20)
        opponent.health -= (damage1 + damage2)
        print(f"{self.name} fires two arrows dealing {damage1} and {damage2} damage!")

# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)
        self.shield_active = False

    def special_ability(self, opponent):
        if not self.shield_active:
            print(f"{self.name} activates 'Divine Shield'! The next attack will be blocked.")
            self.shield_active = True
        else:
            print(f"{self.name} uses 'Holy Strike'!")
            damage = self.attack_power + 15
            opponent.health -= damage
            print(f"{self.name} deals {damage} damage with Holy Strike!")

# EvilWizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen_amount = random.randint(5, 15)
        self.health += regen_amount
        print(f"{self.name} regenerates {regen_amount} health! Current health: {self.health}")

# Create Character Function
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle Function
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")
            continue

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main Function
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
