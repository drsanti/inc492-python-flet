import flet as ft
import time
from init import *

def main(page: ft.Page):
    app_init(page, "Text Control Example", "#222222")

    def event_handler(event):
        if(event.control.text == "Button 1"):
            print("Button 1 clicked")

    for i in range(20):
        b = ft.ElevatedButton(f"Button {i+1}", on_click=event_handler)
        page.add(b)

ft.app(main)
