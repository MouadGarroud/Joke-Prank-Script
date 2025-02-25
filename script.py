# Mouad Garroud
import os , pygame , threading , time , subprocess
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

pygame.mixer.init()
folder_path = Path(r"C:/Users/Mouad Garroud/Desktop/New folder")
image_path = r"C:/Users/Mouad Garroud/Desktop/projet/by pass/joke.png"
file_path = r"C:/Users/Mouad Garroud/Desktop/projet/by pass/joke.mp3"
time.sleep(5)
def play_audio():
    subprocess.run(
        [r"C:/Program Files/AutoHotkey/UX/AutoHotkeyUX.exe", r"C:/Users/Mouad Garroud/Desktop/projet/by pass/alt.ahk"],
        check=True
    )
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(start=2)
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
    os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep") 
def show_image():
    img_root = tk.Tk()
    img_root.attributes('-fullscreen', True)
    img_root.attributes('-topmost', True)
    screen_width, screen_height = img_root.winfo_screenwidth(), img_root.winfo_screenheight()
    image = Image.open(image_path).resize((screen_width, screen_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(img_root, image=photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    img_root.bind("<Escape>", lambda e: img_root.destroy())
    img_root.mainloop()
if not folder_path.is_dir():
    audio_thread = threading.Thread(target=play_audio, daemon=True)
    audio_thread.start()
    show_image()

