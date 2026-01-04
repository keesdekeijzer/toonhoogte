#!/usr/bin/env python3

import os
import subprocess

import tkinter as tk  
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd

"""
# versie 2026-01-04 18:16
Eerste versie
"""


# toonhoogte - pitch

# (ffmpeg moet ook geinstalleerd zijn)

def bestandsnaam_opschonen(naam):
    naam = naam.replace('(','_')
    naam = naam.replace(')','_')
    naam = naam.replace(' ','_')
    return naam

def pas_aan(invoer, uitvoer, toonhoogte):
    command = f"ffmpeg -i {invoer} -af asetrate=44100*{toonhoogte.get()},aresample=44100,atempo=1/{toonhoogte.get()} {uitvoer}"
    process_1 = subprocess.run(command, shell=True, capture_output=True, text=True)
    showinfo(
        title='Klaar',
        message="Bestand is omgezet!"
    )
    return process_1

def start_knop():
    hoofdprogramma()

def hoofdprogramma():
    print(f"invoer: {invoer}\nuitvoer: {uitvoer}\ntoonhoogte: {toonhoogte.get()}")
    print(pas_aan(invoer, uitvoer, toonhoogte))
    print(f"invoer: {invoer}\nuitvoer: {uitvoer}\ntoonhoogte: {toonhoogte.get()}")

def kies_bestand_invoer():
    filetypes = (
        ('mp3 bestanden', '*.mp3'),
        ('Alle bestanden', '*.*')
    )

    bestand = fd.askopenfilename(
        title='Kies een mp3',
        initialdir='.',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=bestand
    )
    label1bestand.configure(text=bestand)
    return bestand


def kies_bestand_uitvoer():
    filetypes = (
        ('mp3 bestanden', '*.mp3'),
        ('Alle bestanden', '*.*')
    )

    bestand = fd.asksaveasfilename(
        title='Kies een mp3',
        defaultextension=".mp3",
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=bestand
    )
    label2bestand.configure(text=bestand)
    return bestand


def kies_invoer():
    global invoer
    invoer = kies_bestand_invoer()

def kies_uitvoer():
    global uitvoer
    uitvoer = kies_bestand_uitvoer()
    #uitvoer = './test-aangepast.mp3'



# data
schaal = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0)


# GUI
root = tk.Tk()
root.title('Spreek - Tekst omzetten naar spraak')

# Venster centreren
window_width = 1000
window_height = 600

# scherm afmetingen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# middelpunt
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# centreren
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# icon
try:
    # Linux en macOS
    photo = tk.PhotoImage(file='./tts.png') #.png or .gif
    root.iconphoto(False, photo)
except tk.TclError:
    print("icon file not found.")

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
style.configure("LB.TLabel", foreground="black", background="lightblue")

# label1
label1 = ttk.Label(
    root,
    text='Invoer',
    font=("Helvetica", 14),
    style="BW.TLabel")
label1.pack(padx=5,pady=5)

# invoer
button_invoer = ttk.Button(root, text='Kies invoer bestand', command=kies_invoer)
button_invoer.pack(padx=5,pady=5)

# label invoerbestand
label1bestand = ttk.Label(
    root,
    text='?',
    font=("Helvetica", 14),
    style="LB.TLabel")
label1bestand.pack(padx=5,pady=5)

# label2
label2 = ttk.Label(
    root,
    text='Uitvoer',
    font=("Helvetica", 14),
    style="BW.TLabel")
label2.pack(padx=5,pady=5)

# uitvoer
button_uitvoer = ttk.Button(root, text='Kies uitvoer bestand', command=kies_uitvoer)
button_uitvoer.pack(padx=5,pady=5)

# label uitvoerbestand
label2bestand = ttk.Label(
    root,
    text='?',
    font=("Helvetica", 14),
    style="LB.TLabel")
label2bestand.pack(padx=5,pady=5)

# label3 toonhoogte
label3 = ttk.Label(
    root,
    text='Toonhoogte',
    font=("Helvetica", 14),
    style="BW.TLabel")
label3.pack(padx=5,pady=5)

# toonhoogte
toonhoogte = tk.StringVar(value=1.0)
toonhoogte_spin_box = ttk.Spinbox(
    root,
    from_=0.0,
    to=2.0,
    values=schaal,
    textvariable=toonhoogte,
    wrap=True)

toonhoogte_spin_box.pack(padx=5,pady=5)

# knop Start
button = ttk.Button(root, text='Start', command=start_knop)
button.pack(padx=5,pady=5)

# knop Exit
exit_button = ttk.Button(root, text='Exit', command=lambda: root.quit())
exit_button.pack(padx=5,pady=5)

# start GUI
root.mainloop()
