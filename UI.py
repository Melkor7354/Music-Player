import tkinter as tk
import vlc
import main
import datetime
def play():
    p = vlc.MediaPlayer("C:\\Users\\EKLAVYA\\Downloads\\Far.Cry.6-EMPRESS\\Empress Theme #1 [The Origins].mp3")
    p.play()

class UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        main.initialize()
        self.title("AudioByte")
        main.dark_title_bar(self)
        self.minsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())
        self.switch_frame(Start)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class BasicPage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

class Start(BasicPage):
    def __init__(self):
        BasicPage.__init__(self)

# Create a Button
btn = tk.Button(root, text='Click me !', bd='5',
             command=play)

# Set the position of button on the top of window.
btn.pack(side='top')

root.mainloop()