import flet as ft

def saludar(event):
    print("Hola")


def main(page: ft.Page):
    row = ft.Row(controls= [
        ft.TextField(label = "Digita tu nombre"),
        ft.ElevatedButton(text= "Saludar", on_click= saludar),
    ])

    page.add(row)

ft.app(target= main)