#
# examples/ex02/main.py
# Page properties
#   - Set the app title
#   - Set the app window size
#   - Set the app background color
#

import flet as ft

def main(page: ft.Page):
    # Set the app title
    page.title = "Example02 - Page properties"

    # Set the app window size
    page.window.width = 400
    page.window.height = 640

    # Set the app background color
    page.bgcolor = "red" # or "#ff0000" or ft.colors.RED
    
    # Update the page properties 
    page.update()

# Run the Flet app with the main function as the target
ft.app(target=main)
