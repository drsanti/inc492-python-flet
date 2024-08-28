#
# examples/ex05/app_init.py
# Passing argument to a function
#   - Pass the `title` to the `app_init` function in the `app_init` module.
#

import flet as ft
from app_init import app_init

def main(page: ft.Page):
    # Call the function in the app_init module and pass the `title` parameter to it.
    app_init(page, "Example 05 - Basic Controls")

ft.app(target=main)
