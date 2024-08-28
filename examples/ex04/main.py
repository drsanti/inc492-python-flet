#
# examples/ex04/main.py
# Helper functions
#   - Create a module (app_init.py)
#   - Using the module
#

import flet as ft

# Import the app_init module
#   syntax: from <filename> import <function>
from app_init import app_init

def main(page: ft.Page):
    # Call the function in the app_init module
    app_init(page)

# Run the Flet app with the main function as the target
ft.app(target=main)
