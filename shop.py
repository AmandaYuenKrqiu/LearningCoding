class Shop:
    def __init__(self):
        self.items = {
            "hair_color": ["Black", "Blonde", "Red", "Blue"],
            "outfit": ["Casual", "Sporty", "Formal", "Superhero"]
        }
        self.prices = {
            "Black": 10,
            "Blonde": 20,
            "Red": 30,
            "Blue": 40,
            "Casual": 50,
            "Sporty": 60,
            "Formal": 70,
            "Superhero": 80
        }

    def display_shop(self):
        print("Welcome to the Shop!")
        print("Available items:")
        for category, items in self.items.items():
            print(f"\n{category.capitalize()}:")
            for item in items:
                print(f"{item} - {self.prices[item]} coins")

    def purchase_item(self, item, player):
        if item in self.prices:
            print(f"Purchasing {item} for {self.prices[item]} coins.")
            if item in self.items["hair_color"]:
                player.change_hair_color(item)
            elif item in self.items["outfit"]:
                player.change_outfit(item)
        else:
            print(f"Item {item} is not available.")

# Example usage
if __name__ == "__main__":
    from character import Character
    player = Character()

    shop = Shop()
    shop.display_shop()
    
    # Simulate purchasing an item
    shop.purchase_item("Blonde", player)
    shop.purchase_item("Sporty", player)

    player.display_character()
