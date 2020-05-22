# Import Modules
import tkinter as tkr
import pygame, os

# TESTING TESTING TESTING 

# Create Window
music = tkr.Tk()


# Edit Window
music.title("MP3 Player")
music.geometry("405x580")


# Name of song file
file = "GameOver.mp3"

# pygame initialization
pygame.init()
pygame.mixer.init()

volumeControl = tkr.Scale(music, from_=(0 *100), to_=(1.0 * 100),
                            orient = tkr.VERTICAL, resolution=0.1)
# Playlist directory
os.chdir("C:/Users/Kaveon Smith/PycharmProjects/MP3_Player")
print(os.getcwd)
ListOfSongs = os.listdir()

# Allows for more than one song to appear in playlist
playlist = tkr.Listbox(music, highlightcolor='blue', selectmode=tkr.SINGLE)
print(ListOfSongs)
for item in ListOfSongs:
    increment = 0
    playlist.insert(increment, item)
    increment +=1


# Placeholder for volume function below
paused = False
# Allows user to play, pause, stop, and control volume of the selected song
class playerOptions:
    # Action Event
    def StartPlayer(self):
        pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volumeControl.get())
        print(pygame.mixer.music.get_volume())
        print(volumeControl.get())


    def ExitPlayer(self):
        pygame.mixer.music.stop()



    def PausePlayer(self):
        global paused
        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True


    def resumePlayer(self):
        pygame.mixer.unpause()

# Lists the buttons in the tkr window
obj = playerOptions
play = tkr.Button(music, width=5, height=3, text ="Play", command=obj().StartPlayer)
pause = tkr.Button(music, width =5, height=3, text="Pause", command=obj().PausePlayer)
stop = tkr.Button(music, width =5, height=3, text="Stop", command=obj().ExitPlayer)

# Lists song names
textvar= tkr.StringVar()
songTitle = tkr.Label(music,textvariable=textvar)

# Displays buttons in the tkr window
songTitle.pack()
play.pack(fill='x')
pause.pack(fill='x')
stop.pack(fill='x')
volumeControl.pack(fill='x')
playlist.pack(fill="both", expand="yes")

# Allows songs to play out
music.mainloop()