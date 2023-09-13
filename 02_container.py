import flet as ft


def main(page: ft.Page):

    #Row Para agregarlos en una sola linea podria decirse que es un container 
    datos = ft.Row(controls=[ft.Text("Python"),
                             ft.Text("Flet"), 
                             ft.Text("Flutter",text_align= "CENTER"),])

    page.add(datos)

ft.app(target= main)