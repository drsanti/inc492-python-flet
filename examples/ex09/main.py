#
# examples/ex09/app_init.py
# - Lambda functions
# - Passing data to event handler

import flet as ft
from app_init import app_init

def main(page: ft.Page):
    app_init(page, "Example 09 - Lambda functions")

    # 
    # Example 1: Pass event and data to event handler.
    #

    # Define an event handler for the button 1 and 2 
    # Note: The unused parameter/variable should be replaced by `_`.
    def event_handler12(_, data):
        print(data)

    # Use lambda to defer execution until the event occurs
    # Note: The `event` is a variable name.
    b1 = ft.ElevatedButton("Button 1", on_click=lambda event: event_handler12(event, "b1"))
    b2 = ft.ElevatedButton("Button 2", on_click=lambda event: event_handler12(event, "b2"))

    page.add(b1)
    page.add(b2)


    # 
    # Example 2: Pass only data to event handler.
    #

    # Define an event handler for the button 3 and 4
    # Note: Only one parameter `data` is passed to this function.
    def event_handler34(data):
        print(data)

    # Use lambda to defer execution until the event occurs
    # Note: The event is not used, we can replace it with `_`.
    b3 = ft.ElevatedButton("Button 3", on_click=lambda _: event_handler34("b3"))
    b4 = ft.ElevatedButton("Button 4", on_click=lambda _: event_handler34("b4"))

    page.add(b3)
    page.add(b4)

ft.app(target=main)

