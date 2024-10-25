from abc import ABC


class Songs(ABC):
    def __init__(self, title, artist, lenght):
        self.title = title
        self.artist = artist
        self.lenght = lenght

class Rock(Songs):
    def __init__(self, title, artist, lenght):
        super().__init__(title, artist, lenght)

class Pop(Songs):
    def __init__(self, title, artist, lenght):
        super().__init__(title, artist, lenght)

class Albums:
    def __init__(self, artist, release_data):
        self.title = []
        self.artist = artist
        self.release = release_data

class Playlist:
    def __init__(self, name, song):
        self.name = name
        self.song = song
        self.playlist = []

    def Create_Playlist(self, value):
        self.playlist.append(value)

    def View_Playlist(self):
        return self.playlist

    def Find_Song(self, song):
        if song in self.playlist:
            return song
        return "Song not found"


class User(Playlist):
    def __init__(self, user, name, songs):
        super().__init__(name, songs)
        self.user = user


    def Listen_to_Song(self):
        return f"User are listen from artist {self.name} : song {self.song}"




# use = User("Ann","Tatul", "Pax axbyuri mot")
playlist = Playlist("Hayko", "Inchpes Urin u Bardin")
playlist.Create_Playlist("Inchpes urin u bardin")
playlist.Create_Playlist("Karmir varders")
print(playlist.View_Playlist())
print(playlist.Find_Song("Karmir varders"))
# print(playlist.View_Playlist())

# print(use.Listen_to_Song())