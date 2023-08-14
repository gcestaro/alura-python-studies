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

    def __str__(self):
        return f"{self.name} - {self.__duration} - {self.likes}"


class Series(TvShow):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.__seasons = seasons

    def __str__(self):
        return f"{self.name} - {self.__seasons} - {self.likes}"


class Playlist:

    def __init__(self, name, tv_shows):
        self.__name = name
        self.__tv_shows = tv_shows

    def size(self):
        return len(self.__tv_shows)


if __name__ == '__main__':
    avengers = Movie("avengers - infinity war", 2018, 160)
    avengers.like()

    harry_potter_6 = Movie("harry potter and the half-blood prince", 2009, 150)
    harry_potter_6.like()

    star_wars_ep_4 = Movie("Star Wars - Episode IV – A New Hope", 1977, 180)
    star_wars_ep_4.like()

    breaking_bad = Series("breaking bad", 2008, 5)
    breaking_bad.like()

    prison_break = Series("prison break", 2005, 5)
    prison_break.like()

    tv_shows = [avengers, breaking_bad, prison_break, star_wars_ep_4, harry_potter_6]

    weekend_playlist = Playlist("Weekend", tv_shows)

    for tv_show in tv_shows:
        print(tv_show)
