#
# examples/ex09/app_init.py
# Module used to initialize the app
#   Note:
#       This module can be imported by another file/module using the
#       `from app_init import app_init`
#       syntax:
#           from <filename> import <function>
#
#   Usage:
#       from app_init import app_init
#       app_init(page, "title")
#

import flet as ft

def app_init(page: ft.Page, title: str):
    # Set the app title
    page.title = title

    # Set the app window size
    page.window.width = 400
    page.window.height = 640

    # Set the app background color
    page.bgcolor = "#222222"
    
    # Update the page properties 
    page.update()
