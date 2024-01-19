import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

root = ttkbootstrap.Window(themename='morp')
root.title("Weather App")
root.geometry("400x400")

#Entry widget --> to enter the city name
city_entry = ttkbootstrap.Entry(root, font = "Helvetica, 18")