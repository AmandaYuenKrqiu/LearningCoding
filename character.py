class Character:
    def __init__(self, name="Player", hair_color="Black", outfit="Casual"):
        self.name = name
        self.hair_color = hair_color
        self.outfit = outfit

    def change_hair_color(self, new_color):
        self.hair_color = new_color

    def change_outfit(self, new_outfit):
        self.outfit = new_outfit

    def display_character(self):
        print(f"Character Name: {self.name}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Outfit: {self.outfit}")

# Example usage
if __name__ == "__main__":
    player_character = Character()
    player_character.display_character()

    # Changing attributes
    player_character.change_hair_color("Blonde")
    player_character.change_outfit("Sporty")
    player_character.display_character()
