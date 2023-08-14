class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.__year = year
        self.__duration = duration
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


class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.__year = year
        self.__seasons = seasons
        self.__likes = 0

    def like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def name(self):
        return self.__name


if __name__ == '__main__':
    avengers = Movie("avengers - infinity war", 2018, 160)
    print(avengers.name)

    breaking_bad = Series("breaking bad", 2008, 5)
    print(breaking_bad.name)
