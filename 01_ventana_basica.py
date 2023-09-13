import flet as ft

def main(page: ft.Page):

    page.add(ft.Text(value= "Hola mundo!", color= "Blue"))

    page.add(ft.Row([ft.Text("Usuario"),
     ft.TextField(label ="", autofocus=True),]))

    page.add(ft.Row([ft.Text("Contraseña"),
     ft.TextField( password=True, can_reveal_password=True),]))
    
    page.update()


#escritorio
ft.app(target= main)

#web 
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)
