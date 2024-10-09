#
# examples/ex06/main.py
# Basic Controls/Widgets
#   - Button
#   - Checkbox
#   - Radio
#   - Slider
#   - Switch
#   - TextField
#   - Text
#   - Image
#   - Column
#   - Row
#   - Stack
#   - Page
#   - etc.
#

import flet as ft
from app_init import app_init

def main(page: ft.Page):
    app_init(page, "Example 06 - Basic Controls")

    # Create a simple text control
    text1 = ft.Text("Text 1")

    # Create a text control with custom properties
    text2 = ft.Text("Text 2", color="red", size=40, italic=True, )
    
    # Method 1
    # Add the text controls to the page using `controls.append` followed by `update`
    page.controls.append(text1)
    page.controls.append(text2)
    page.update()
    
    # Method 2
    # Add the text controls to the page using `add`.
    # page.add(text1)
    # page.add(text2)

ft.app(target=main)
