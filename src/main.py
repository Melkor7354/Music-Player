import eyed3
import os
from PIL import Image
import pickle
import audioread
import random
import eel

audiofile = eyed3.load(r"C:\Users\EKLAVYA\Music\Atrax Morgue\in search of death\04 in search of death.mp3")
'''audiofile.tag.artist = "Token Entry"
audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = "Various Artists"
audiofile.tag.title = "The Edge"
audiofile.tag.track_num = 3
audiofile.tag.save()'''
print(audiofile.tag._getArtist())

eel.init('../Web')


def convert_to_binary(file_path):
    image = open(file_path, 'rb')
    return image.read()


def convert_to_image(binary, song_title):
    result_file = song_title

    with open(result_file, 'wb') as file_handler:
        file_handler.write(binary)

    Image.open(result_file).save(result_file + '.png', 'PNG')

    os.remove(result_file)


def initialize():
    parent_dir = os.path.expanduser('~')
    _dir = 'music_files'
    _dir2 = 'music_files/images'
    _dir3 = 'music_files/artists'
    path = os.path.join(parent_dir, _dir)
    path2 = os.path.join(parent_dir, _dir2)
    path3 = os.path.join(parent_dir, _dir3)
    try:
        mode = 0o666
        os.mkdir(mode=mode, path=path)
        os.mkdir(mode=mode, path=path2)
        os.mkdir(mode=mode, path=path3)
    except FileExistsError:
        pass


class Song:
    def __init__(self, song_path, title, artist, album):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = audioread.audio_open(song_path).duration()
        self.song_path = ''
        for i in song_path:
            if i==' ':
                self.song_path += '_'
            else:
                self.song_path += i

    def save(self):
        with open('{}'.format(self.title), 'wb') as file:
            pickle.dump(self, file)

    def info(self):
        return [self.title, self.artist, self.album, self.duration]


class Playlist(list):
    def __init__(self, title, description=None):
        list.__init__(self)
        self.title = title
        self.description = description
        self.cover = self.add_cover()
        duration = 0
        song_count = 0
        for song in self:
            duration += song.info()[4]
            song_count += 1
        self.duration = duration
        self.song_count = song_count

    def check_duplicates(self, song_list):
        non_duplicates = []
        result = 0
        for i in song_list:
            for j in self:
                if i.info() == j.info():
                    result = 1
            else:
                non_duplicates.append(i)
        if result == 0:
            return (0, non_duplicates)
        else:
            return (1, non_duplicates)

    def add_song(self, song):
        result = self.check_duplicates([song])
        if result[0] == 0:
            self.append(song)
            return True
        else:
            return False

    def add_multiple_songs(self, songs):
        result = self.check_duplicates(songs)
        if result[0] == 0:
            self.append(songs)
        else:
            self.append(result[1])

    def remove_songs(self, songs):
        for song in songs:
            self.remove(song)

    def save(self):
        with open('{}'.format(self.title), 'wb') as file:
            pickle.dump(self, file)

    def delete(self):
        os.remove('{}'.format(self.title))

    def add_cover(self):
        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()
        return convert_to_binary(filename)

    def info(self):
        return [self.title, self.description, self.cover, self.duration, self.song_count]


    def play(self):





eel.start('index.html')
