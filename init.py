import flet as ft

BG = "cyan"

def app_init(page: ft.Page, title: str, bg_color: str):
    page.title = title
    page.window.width = 400
    page.window.height = 800
    page.bgcolor = bg_color
    page.update()

def app_title(page: ft.Page, title: str):
    page.title = title
    page.update()

def app_bg_color(page: ft.Page, bg_color: str):
    page.bgcolor = bg_color
    page.update()


