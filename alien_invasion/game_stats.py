class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0
        self.high_score = self. read_high_score()

        self.game_active = False

    def read_high_score(self):
        try:
            with open('high_score.txt') as file_object:
                contests = file_object.read()
        except FileNotFoundError:
            contests = 0
        return int(contests)

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
