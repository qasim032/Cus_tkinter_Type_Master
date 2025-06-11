from customtkinter import *
from PIL import Image
from time import *


app = CTk()
app.geometry("1280x720")
app.title("Type Master by Qasim")
set_appearance_mode("Dark")
set_default_color_theme("blue")
frame = CTkFrame(master=app)
frame.pack(fill="both", expand=True)


def calculate_speed(user_input, time1, time2):
    time_delay = time2 - time1
    words = len(user_input.split())
    if time_delay > 0:
        return round(words / time_delay, 3)
    return 0

def calculate_mistakes(user_input, chapter_text):
    error = 0
    for i in range(len(chapter_text)):
        try:
            if chapter_text[i] != user_input[i]:
                error = error + 1
        except :
            error = error + 1
    return error-1 
    
def done(user_input,chapter_text,time1,time2):
    clear_screen()
    accuracy = 100 - (calculate_mistakes(user_input, chapter_text) / len(chapter_text) * 100)
    speed = calculate_speed(user_input,time1,time2)
    mistakes = calculate_mistakes(user_input,chapter_text)
    CTkLabel(master=frame,text=f"\nTyping Speed: {speed} letters/sec\nAlphabet Mistakes: {mistakes}\nAccuracy: {accuracy:.3f}%",font=("Arial", 20),justify="center").place(relx=0.5, rely=0.2, anchor="center")
    CTkButton(frame, text="Chapters", command=next_chapter, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.50, anchor="center")
    CTkButton(frame, text="Go Back", command=home, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.55, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.60, anchor="center")

def next_chapter():
    clear_screen() 
    text = "Welcome to Type Master!\n\nThis is a simple type practice app designed to help you improve your typing speed and accuracy.\n\nClick on 'Chapters' to begin your type practice or 'Exit' to close the app." 
    CTkLabel(master=frame, text=text, font=("Arial", 20), justify="center").place(relx=0.5, rely=0.2, anchor="center")
    CTkButton(frame, text="Chapter1", command=chapter1display, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.55, anchor="center")
    CTkButton(frame, text="Chapter2", command=chapter2display, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.60, anchor="center")
    CTkButton(frame, text="Chapter3", command=chapter3display, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.65, anchor="center")
    CTkButton(frame, text="Go Back", command=home, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.70, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.75, anchor="center")

def chapter2():
    with open("chapter2.txt", "r", encoding="utf-8") as file:
            return file.read()
def chapter2display():
    clear_screen()
    CTkLabel(master=frame, text=chapter2(), font=("Arial", 20), justify="center").place(relx=0.5, rely=0.2, anchor="center")
    user_input = CTkEntry(master=frame, placeholder_text="Type here...", width=300, text_color="#FFFFFF")
    user_input.place(relx=0.5, rely=0.50, anchor="center")
    time1 = time()
    CTkButton(frame, text="Done", command=lambda: done(user_input.get(), chapter2(), time1, time()), fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.70, anchor="center")
    CTkButton(frame, text="Go Back", command=home, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.75, anchor="center")
    CTkButton(frame, text="Chapter3", command=chapter3display, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.80, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.85, anchor="center")
    

def chapter3():
    with open("chapter3.txt", "r", encoding="utf-8") as file:
            return file.read()
def chapter3display():
    clear_screen()
    CTkLabel(master=frame, text=chapter3(), font=("Arial", 20), justify="center").place(relx=0.5, rely=0.2, anchor="center")
    user_input = CTkEntry(master=frame, placeholder_text="Type here...", width=300, text_color="#FFFFFF")
    user_input.place(relx=0.5, rely=0.50, anchor="center")
    time1 = time()
    CTkButton(frame, text="Done", command=lambda: done(user_input.get(), chapter3(), time1, time()), fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.70, anchor="center")
    CTkButton(frame, text="Go Back", command=home, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.75, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.80, anchor="center")
    
def chapter1():
    with open("chapter1.txt", "r", encoding="utf-8") as file:
            return file.read()  
def chapter1display():
    clear_screen()
    CTkLabel(master=frame, text=chapter1(), font=("Arial", 20), justify="center").place(relx=0.5, rely=0.2, anchor="center")
    user_input = CTkEntry(master=frame, placeholder_text="Type here...", width=300, text_color="#FFFFFF")
    user_input.place(relx=0.5, rely=0.50, anchor="center")
    time1 = time()
    CTkButton(frame, text="Done", command=lambda: done(user_input.get(), chapter1(), time1, time()), fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.70, anchor="center")  
    CTkButton(frame, text="Go Back", command=home, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.75, anchor="center")
    CTkButton(frame, text="Chapter2", command=chapter2display, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.80, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.85, anchor="center")
    
    
def clear_screen():
    for widget in frame.winfo_children():
        widget.destroy()

def home():

    clear_screen()     
    my_image = CTkImage(dark_image=Image.open("banner.png"), size=(1280, 200))
    CTkLabel(frame, image=my_image, text="").place(relx=0.5, rely=0.35, anchor="center")
    CTkButton(frame, text="Start", command=next_chapter, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.55, anchor="center")
    CTkButton(frame, text="About", command=about_screen, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.65, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.75, anchor="center")


def about_screen():
    clear_screen()  


    text = ("🖥️ Type Master by Qasim\nWelcome to Type Master — a simple and smooth type practice app built to help you improve your typing speed and accuracy. 🚀\nDesigned with a clean interface and a dark theme for better focus and comfort.\nPerfect for anyone looking to sharpen their type skills. ⌨️\n\n👨‍💻 About Me\nI'm Qasim, a passionate tech enthusiast and AI student. I built this app as part of my journey in Python and GUI development.\n\n📌 Version: 1.0\n🛠️ Built with: Python & CustomTkinter\n❤️ Made with love"
    )
    CTkLabel(master=frame, text=text, font=("Arial", 18)).place(relx=0.5, rely=0.3, anchor="center")

    CTkButton(frame, text="Go Back", command=home, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.55, anchor="center")
    CTkButton(frame, text="Exit", command=exit_app, fg_color="#8B1740", hover_color="#059FFF").place(relx=0.5, rely=0.60, anchor="center")


def exit_app():
    app.destroy()


home()
app.mainloop()
