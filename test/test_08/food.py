class Foood:

    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Foood.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts

        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food


def main():
    mushroom_skewer = Foood(ingredients=["Mushroom", "Hearty mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

    mushroom_skewer = Foood.from_nothing(hearts=3)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")


if __name__ == '__main__':
    main()