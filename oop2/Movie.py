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
        print("name getter called")
        return self.__name

    @name.setter
    def name(self, name):
        print("name setter called")
        self.__name = name.title()


class Movie(TvShow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.__duration = duration


class Series(TvShow):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.__seasons = seasons


if __name__ == '__main__':
    avengers = Movie("avengers - infinity war", 2018, 160)
    print(avengers.name)

    breaking_bad = Series("breaking bad", 2008, 5)
    print(breaking_bad.name)
