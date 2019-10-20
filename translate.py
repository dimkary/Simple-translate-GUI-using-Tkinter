# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:16:01 2019

@author: Karips
"""

import tkinter as tk
global question
import sys
sys.path.insert( 0,".\\translate")

from mtranslate import translate
 
def query(string):
    greek_label['text']="Ελληνικά: " + translate(string, 'el')
    german_label['text']="Deutch: " + translate(string, 'de')
    swedish_label['text']="Svenska: " + translate(string, 'sv')


color = "#224f0a"
HEIGHT = 700
WIDTH = 1000
resultsFont=("Arial", 25)

root = tk.Tk()
root.title("Translate Pal!!!")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

bckg_img = tk.PhotoImage(file="./globe.png")
bckg_lbl = tk.Label(root, image = bckg_img, bg = "#ccffff")
bckg_lbl.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = color, bd =3)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor =tk.N)

entry = tk.Entry(frame,font=resultsFont)
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "TRANSLATE ME",  font='Helvetica 18 bold', bg ="gray", command = lambda: query(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)
button.focus_set()
results_frame = tk.Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=3,bg = "white")
results_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = tk.N)    

font = "Times"
size = 50
greek_label = tk.Label(results_frame, text = "Ελληνικά: ",
		 font=resultsFont,bg = "white")
greek_label.place(rely = 0.01)

german_label= tk.Label(results_frame, text = "Deutch: ", font=resultsFont,bg = "white")
german_label.place(rely = 0.4)

swedish_label = tk.Label(results_frame, text = "Svenska: ", font=resultsFont,bg = "white")
swedish_label.place(rely = 0.8)


root.mainloop()

