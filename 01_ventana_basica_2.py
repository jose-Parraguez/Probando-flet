import flet as ft

def main(page: ft.Page):

    titulo = ft.Text(value= "Hola mundo!", color= "Blue")

    Usuario = ft.Row([ft.Text("Usuario      "),
                ft.TextField(""),])

    contraseña = ft.Row([ft.Text("Contraseña"),
     ft.TextField( password=True, can_reveal_password=True),])
    
    page.add(titulo)
    page.add(Usuario)
    page.add(contraseña)
    page.update()

#escritorio
ft.app(target= main)

#web 
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)
