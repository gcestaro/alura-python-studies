class TvShow:
    def __init__(self, name, year):
        self.__name = name.title()
        self.__year = year
        self.__likes = 0

    def like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()


class Movie(TvShow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.__duration = duration

    def print(self):
        print(f"{self.name} - {self.__duration} - {self.likes}")


class Series(TvShow):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.__seasons = seasons

    def print(self):
        print(f"{self.name} - {self.__seasons} - {self.likes}")


if __name__ == '__main__':
    avengers = Movie("avengers - infinity war", 2018, 160)
    breaking_bad = Series("breaking bad", 2008, 5)

    avengers.like()
    avengers.like()
    breaking_bad.like()

    tv_shows = [avengers, breaking_bad]

    for tv_show in tv_shows:
        tv_show.print()
