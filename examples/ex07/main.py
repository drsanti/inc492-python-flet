#
# examples/ex07/main.py
# Using `page.update` function.
#   Note:   It is a good practice to use `page.update` function 
#           to update the page when you need to update the page.
#           This technique can help to improve the performance of the app.
#

import time
import flet as ft
from app_init import app_init

def main(page: ft.Page):
    app_init(page, "Example 07 - page.update()")

    for i in range (10):
        # Create a text control, add it to the page, and update the page
        page.add(ft.Text(f"Text {i}"))
        time.sleep(0.5)

    for i in range (10):
        # Create a text control, add it to the page without updating the page
        page.controls.append(ft.Text(f"Text {i}"))
        if i % 2 == 0:
            # Update the page
            page.update()
        time.sleep(0.5)

ft.app(target=main)
