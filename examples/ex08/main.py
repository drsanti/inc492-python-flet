#
# examples/ex08/app_init.py
# Event and Event Handler
#

import flet as ft
from app_init import app_init

def main(page: ft.Page):
    app_init(page, "Example 08 - Basic Event & Handler")

    # Define an event handler   
    def event_handler(event):
        print(event.control.text)
        
        # Note1: Check all properties of the `event`
        #print(dir(event))

        # Note2: Check all properties of the `event.control`
        #print(dir(event.control))

    # Create a button and give it an event handler
    button = ft.ElevatedButton("Click me", on_click=event_handler)

    # Add the button to the page and update the page
    page.add(button)

ft.app(target=main)
