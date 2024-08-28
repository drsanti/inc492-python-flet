#
# examples/ex03/main.py
# Helper functions
#   - Create a function
#   - Call the function
#

import flet as ft

def app_init(page: ft.Page):
    # Set the app title
    page.title = "Example03 - Helper function"

    # Set the app window size
    page.window.width = 400
    page.window.height = 640

    # Set the app background color
    page.bgcolor = "red" # or "#ff0000" or ft.colors.RED
    
    # Update the page properties 
    page.update()

def main(page: ft.Page):
    app_init(page)

# Run the Flet app with the main function as the target
ft.app(target=main)
