import flet as ft


def main(page: ft.Page):

    lenguajes = ["python", "flet", "Perro", "Jamon"]
    etiquetas = []

    #Guardo cada variable en etiqueta con ft.Text para que en el control funcione
    for e in lenguajes:
        etiquetas.append(ft.Text(e))

    datos = ft.Row(controls = etiquetas)
    page.add(datos)

ft.app(target= main)