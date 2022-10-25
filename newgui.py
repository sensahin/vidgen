print("Launching VidGen...")
print("Talking to the internet...")
from tkinter.ttk import Combobox
import generation_utils
import re
import os
import platform
from movie_maker import make_movie
import fakeyou
import uberduck
print("Done set up, time to generate!")
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, StringVar, OptionMenu, IntVar, Checkbutton, filedialog, messagebox


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("487x783")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 783,
    width = 487,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    248.0,
    391.0,
    image=image_image_1
)

canvas.create_text(
    73.0,
    11.0,
    anchor="nw",
    text="Video Generator",
    fill="#FFFFFF",
    font=("Inter", 48 * -1)
)

canvas.create_text(
    176.0,
    539.0,
    anchor="nw",
    text="Extra Settings:",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    12.0,
    100.0,
    anchor="nw",
    text="Topic:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    12.0,
    172.0,
    anchor="nw",
    text="Prompt Type:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    12.0,
    240.0,
    anchor="nw",
    text="Music:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    12.0,
    321.0,
    anchor="nw",
    text="Media:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    12.0,
    402.0,
    anchor="nw",
    text="Voice:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

# entry 1 is topic
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    319.0,
    112.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=161.0,
    y=88.0,
    width=316.0,
    height=47.0
)


entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    388.5,
    671.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_6.place(
    x=300.0,
    y=647.0,
    width=177.0,
    height=47.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    388.5,
    745.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_7.place(
    x=300.0,
    y=721.0,
    width=177.0,
    height=47.0
)



button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=10.0,
    y=585.0,
    width=214.0,
    height=38.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=249.0,
    y=585.0,
    width=228.0,
    height=38.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=249.0,
    y=474.0,
    width=228.0,
    height=38.0
)

canvas.create_text(
    12.0,
    663.0,
    anchor="nw",
    text="Google Voice Speaking Rate:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    12.0,
    744.0,
    anchor="nw",
    text="Google Voice Pitch:",
    fill="#FFFFFF",
    font=("Inter", 20 * -1)
)
window.resizable(False, False)

prompt_types = {}

promptsFile = open('prompts.txt', 'r')
for line in promptsFile.readlines():
    prompt = line.split(";")
    prompt_types[prompt[0]] = prompt[1]
promptsFile.close()

google_voices = generation_utils.get_US_google_cloud_voice_names()
fakeyou_voices = [] #fakeyou.get_all_model_names()

uberduck_voices = []
if uberduck.valid():
    uberduck_voices += uberduck.get_all_model_names()
uberduck_voices.sort()

voices = ["Default"] + ["-- GOOGLE VOICES --"] + google_voices + ["-- FAKEYOU VOICES --"] + fakeyou_voices + ["-- UBERDUCK VOICES --"] + uberduck_voices

music_files = []

for filename in os.listdir("music"):
    f = os.path.join("music", filename)
    if os.path.isfile(f) and filename.endswith("mp3"):
        music_files.append(os.path.basename(f).replace(".mp3",""))

def GenerateGoogleTTS(title, response_text, voice, speaking_rate, pitch):
    filename = generation_utils.title_to_filename(title)
    audio_path = os.path.join("projects",filename, filename + ".aiff")
    if not os.path.exists(audio_path):
        audio_path = os.path.join("projects",filename, filename + ".mp3")
    
    if os.path.exists(audio_path):
        os.rename(audio_path, audio_path + ".old")
    generation_utils.save_audio_google_cloud(title, response_text,voice, speaking_rate, pitch)

def GenerateFakeYouTTS(title, response_text, voice):
    filename = generation_utils.title_to_filename(title)
    audio_path = os.path.join("projects",filename, filename + ".aiff")
    if not os.path.exists(audio_path):
        audio_path = os.path.join("projects",filename, filename + ".mp3")
    if os.path.exists(audio_path):
        os.rename(audio_path, audio_path + ".old")

    fakeyou.TTS(voice, response_text.replace("\n", ""), os.path.join("projects", filename, filename + ".wav"))

def GenerateUberDuckTTS(title, response_text, voice):
    filename = generation_utils.title_to_filename(title)
    audio_path = os.path.join("projects",filename, filename + ".aiff")
    if not os.path.exists(audio_path):
        audio_path = os.path.join("projects",filename, filename + ".mp3")
    if os.path.exists(audio_path):
        os.rename(audio_path, audio_path + ".old")

    uberduck.TTS(voice, response_text.replace("\n", ""), os.path.join("projects", filename, filename + ".wav"))

def GenerateTTS(title, response_text, voice, speaking_rate, pitch):
    if voice == "Default":
        GenerateGoogleTTS(title, response_text, "en-US-Wavenet-A", speaking_rate, pitch)
    elif voice in google_voices:
        GenerateGoogleTTS(title, response_text, voice, speaking_rate, pitch)
    elif voice in fakeyou_voices:
        GenerateFakeYouTTS(title, response_text, voice)
    elif voice in uberduck_voices:
        GenerateUberDuckTTS(title, response_text, voice)


# entry 2 is prompt type.. it's a dropdown and its values from prompt_types
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    319.0,
    185.5,
    image=entry_image_2
)
entry_2 = Combobox(
    values=list(prompt_types.keys()),
    state="readonly",
    textvariable=StringVar(value=""),
    font=("Inter", 20 * -1)
)
entry_2.place(
    x=161.0,
    y=161.0,
    width=316.0,
    height=47.0
)
# entry 3 background music dropdown menu..
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    319.0,
    259.5,
    image=entry_image_3
)
entry_3 = Combobox(
    values=music_files,
    state="readonly",
    textvariable=StringVar(value=""),
    font=("Inter", 20 * -1)
)
entry_3.place(
    x=161.0,
    y=235.0,
    width=316.0,
    height=47.0
)
# entry 4 is media dropdown menu [sg.Text('Media Method'), sg.Combo(["Pexels", "Storyblocks", "Just Images"],default_value='Pexels',key='mediaMethod')],
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    319.0,
    333.5,
    image=entry_image_4
)
entry_4 = Combobox(
    values=["Pexels", "Storyblocks", "Just Images"],
    state="readonly",
    textvariable=StringVar(value=""),
    font=("Inter", 20 * -1)
)
entry_4.place(
    x=161.0,
    y=309.0,
    width=316.0,
    height=47.0
)

# entry 5 is voice dropdown menu
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    319.0,
    409.5,
    image=entry_image_5
)
entry_5 = Combobox(
    values=voices,
    state="readonly",
    textvariable=StringVar(value=""),
    font=("Inter", 20 * -1)
)

entry_5.place(
    x=161.0,
    y=385.0,
    width=316.0,
    height=47.0
)

# button_1 is to generate resourses
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("clicked"),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=474.0,
    width=220.0,
    height=38.0
)



window.resizable(False, False)
window.mainloop()
        