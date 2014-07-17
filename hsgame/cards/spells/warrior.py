import copy
from hsgame.constants import CHARACTER_CLASS, CARD_RARITY
from hsgame.game_objects import Card


class BattleRage(Card):
    def __init__(self):
        super().__init__("Battle Rage", 2, CHARACTER_CLASS.WARRIOR, CARD_RARITY.COMMON)

    def use(self, player, game):
        def damaged_character(character):
            return character.health < character.calculate_max_health()

        super().use(player, game)

        characters = copy.copy(player.minions)
        characters.append(player.hero)

        characters = [character for character in characters if damaged_character(character)]

        for i in range(0, len(characters)):
            player.draw()
