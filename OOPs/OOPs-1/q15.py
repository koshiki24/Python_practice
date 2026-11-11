'''Write a Java program to create a class called "MusicLibrary" with a collection of songs and methods to add and remove songs, and to play a random song.
'''

import random

class MusicLibrary:

    def __init__(self):
        self.collection = []

    def add_songs(self):
        song = input("Enter song you want to add :")
        self.collection.append(song)

    def remove_song(self):
        song = input("Enter song you want to remove :")
        if song in self.collection:
            self.collection.remove(song)
            print(song,"removed successfully")
        else:
            print("Song not found")

    def play_random_song(self):
        if len(self.collection) > 0:
            song = random.choice(self.collection)
            print("Now Playing",song)
        else:
            print("No song available in the library")

    def display(self):
        print("Music Library :",self.collection)

m1 = MusicLibrary()
m1.add_songs()
m1.add_songs()
m1.display()
m1.remove_song()
m1.display()
m1.play_random_song()


