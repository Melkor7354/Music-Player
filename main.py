import eyed3
import os
from PIL import Image
import pickle
import audioread

audiofile = eyed3.load(r"C:\Users\EKLAVYA\Music\Atrax Morgue\in search of death\04 in search of death.mp3")
'''audiofile.tag.artist = "Token Entry"
audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = "Various Artists"
audiofile.tag.title = "The Edge"
audiofile.tag.track_num = 3
audiofile.tag.save()'''
print(audiofile.tag._getArtist())


def convert_to_binary(file_path):
    image = open(file_path, 'rb')
    return image.read()


def convert_to_image(binary, song_title):
    result_file = song_title

    with open(result_file, 'wb') as file_handler:
        file_handler.write(binary)

    Image.open(result_file).save(result_file + '.png', 'PNG')

    os.remove(result_file)


class Song:
    def __init__(self, song_path, title, artist, album, cover):
        self.title = title
        self.artist = artist
        self.album = album
        self.cover_art = cover
        self.duration = audioread.audio_open(song_path).duration()

    def save(self):
        with open('{}'.format(self.title), 'wb') as file:
            pickle.dump(self, file)

    def info(self):
        return [self.title, self.artist, self.album, self.cover_art, self.duration]


class Playlist(list):
    def __init__(self, title, description, cover_image):
        list.__init__()
        self.title = title
        self.description = description
        self.cover = convert_to_binary(cover_image)
        duration = 0
        song_count = 0
        for song in self:
            duration += song.info()[4]
            song_count += 1
        self.duration = duration
        self.song_count = song_count

    def check_duplicates(self):
        pass

    def add_song(self):
        pass

    def add_multiple_songs(self):
        pass

    def save(self):
        with open('{}'.format(self.title), 'wb') as file:
            pickle.dump(self, file)


print(convert_to_binary(r"C:\Users\EKLAVYA\Pictures\GUI\home_icon-removebg-preview.png"))


convert_to_image(convert_to_binary(r"C:\Users\EKLAVYA\Pictures\Playlists\34d99c2e-1362-47d0-aebd-d980590d5e9c.jpg"),
                 'hello')


'''song = Song('a', 'b', 'c', 'd')
song.save()

#load it
with open(f'title', 'rb') as file2:
    song_new = pickle.load(file2)
print(song_new.info())'''
