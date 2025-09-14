from tkinter import *
from tkhtmlview import HTMLLabel
import speech_recognition as sr
from threading import Thread
import google.generativeai as palm
import markdown2
import pyttsx3
from bs4 import BeautifulSoup



def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()
    return text_content


palm.configure(api_key="AIzaSyCIe_DeAv2pHU8dkQ1O3_KL3BnYI-qrqpU")
response = palm.chat(
    context = "Be a helpful developer assistant that give very structured response in markdown.",
    messages="Hi"
    )

def chat(msg):
    global response
    response = response.reply(msg)
    my_html_code = markdown2.Markdown().convert(response.last)
    return my_html_code
 

def open_window():
    home.destroy()  # Ferme la fenêtre home
    create_window()  # Ouvre la fenêtre window

def listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source=source)
        r.energy_threshold = 150
        audio = r.listen(source)
        commande = ""
        try:
            commande = r.recognize_google(audio, language='en-US')
        except Exception:
            commande = "I didn't hear you."
    return commande
    
def create_window():
    global window
    bg_color = "#58CDFF"
    window = Tk()
    window.title("SmartQuery")
    # Calcul des coord d'affichage de la fenetre pour le centre
    width = 1000
    height = 800
    x = (window.winfo_screenwidth()//2) - (width//2)
    y = ((window.winfo_screenheight())//2) - (height//2)
    window.geometry("{}x{}+{}+{}".format(width,height,x,y))
    canvas = Canvas(
    window,
    bg = "white",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    canvas.config(background=bg_color)
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"img/background.png")
    background = canvas.create_image(
        605.5, 178.0,
        image=background_img)
    canvas.create_text(
    520.0, 59.5,
    text = "Comment puis-je vous aider aujourd'hui ?",
    fill = "#000000",
    font = ("Inter-Bold", 30))

    img0 = PhotoImage(file = f"img/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        bg = bg_color,
        activebackground=bg_color,
        relief = "flat",
        cursor="hand2"
        )

    b0.place(
        x = 901, y = 231,
        width = 87,
        height = 87)

    img1 = PhotoImage(file = f"img/img1.png")
    b1 = Button(
        image = img1,
        bg = bg_color,
        borderwidth = 0,
        highlightthickness = 0,
        activebackground= bg_color,
        relief = "flat",
        cursor="hand2"
        )

    b1.place(
        x = 901, y = 362,
        width = 87,
        height = 87)
    #-------------------------------------------------------
    output_entry = HTMLLabel(
        window,
        width = 98,
        height = 31,
        padx = 30,
        pady= 30,
        html="""
            <p>Sure, here is a recursive Fibonacci function in Python:</p>

    <p><code>python
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    </code></p>

    <p>And here is an iterative Fibonacci function in Python:</p>

    <p><code>python
    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    </code></p>
    <p>Sure, here is a recursive Fibonacci function in Python:</p>

    <p><code>python
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    </code></p>

    <p>And here is an iterative Fibonacci function in Python:</p>

    <p><code>python
    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    </code></p>

    """
        )
    output_entry.place(
        x = 32, y = 123
        )
    #-----------------------------------------------------------

    def is_blank(s):
        return len(s.strip()) == 0
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    
    def text_to_speech(text):
        engine.say(text)
        engine.runAndWait()
    
    def search():
        text = user_input.get("1.0", "end-1c")
        if text == "I didn't hear you well." or is_blank(text):
            pass
        else:
            output_entry.delete("1.0", "end")
            text_html = chat(text)
            output_entry.set_html(text_html)
            text_to_say = extract_text_from_html(text_html)
            text_to_speech_async(text_to_say)
            



    img2 = PhotoImage(file = f"img/search.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        bg = bg_color,
        activebackground= bg_color,
        highlightthickness = 0,
        command=search,
        relief = "flat",
        cursor="hand2"
        )

    b2.place(
        x = 895, y = 492,
        width = 100,
        height = 100)

    def b3_click():
        b3.config(state=DISABLED)

        thread = Thread(target=b3_click_async)
        thread.start()
    window.protocol("WM_DELETE_WINDOW", lambda: on_closing(window, engine))

    def on_closing(root, engine):
    # Fonction appelée lors de la fermeture de l'application
        root.destroy()
        # Libérer les ressources du moteur de synthèse vocale
        engine.stop()

    def text_to_speech_async(text):
        thread = Thread(target=text_to_speech, args=(text,))
        thread.start()
        

    def update_text(commande):
        user_input.delete(1.0, END)
        user_input.insert(1.0, commande)
        window.after(0, lambda: text_to_speech_async(commande))
        window.after(0, lambda: b3.config(state=NORMAL))
    
    def b3_click_async():
        commande = listen()
        # Mettre à jour l'interface graphique depuis le thread
        window.after(0, lambda: update_text(commande))

    img3 = PhotoImage(file = f"img/img3.png")
    b3 = Button(
        image = img3,
        bg = bg_color,
        activebackground=bg_color,
        borderwidth = 0,
        highlightthickness = 0,
        command=b3_click,
        relief = "flat",
        cursor="hand2"
        )

    b3.place(
        x = 797, y = 701,
        width = 87,
        height = 87)
    user_input = Text(
        bd = 0,
        wrap= WORD,
        padx= 15,
        pady=15,
        font=("Helvetica", 12),
        bg = "#eceff5",
        highlightthickness = 0)
    user_input.place(
        x = 32, y = 707,
        width = 740,
        height = 74)
    window.resizable(False, False)
    window.mainloop()


home = Tk()
home.title("SmartQuery")
width = 1000
height = 800
x = (home.winfo_screenwidth()//2) - (width//2)
y = ((home.winfo_screenheight())//2) - (height//2)
home.geometry("{}x{}+{}+{}".format(width,height,x,y))
home.configure(bg = "#809eec")
canvas_home = Canvas(
    home,
    bg = "#809eec",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_home.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas_home.create_image(
    605.5, 178.0,
    image=background_img)

canvas_home.create_text(
    500.0, 593.5,
    text = "Authenfication biometrique vocale",
    fill = "#000000",
    font = ("Inter-Bold", int(32.0)))

canvas_home.create_text(
    500.0, 87.5,
    text = "SmartQuery",
    fill = "#000000",
    font = ("Inter-Bold", int(64.0)))

img0 = PhotoImage(file = f"img0.png")
microBtn = Button(
    image = img0,
    borderwidth = 0,
    bg="#809eec",
    highlightthickness = 0,
    activebackground="#809eec",
    command=open_window,
    relief = "flat")

microBtn.place(
    x = 840, y = 661,
    width = 115,
    height = 115)

home.resizable(False, False)
home.mainloop()
