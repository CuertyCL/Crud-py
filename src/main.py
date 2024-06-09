from view.Ventanas import Ventana
from view.Login import Login
from model.Verificacion import Verificacion



if __name__ == "__main__":
    login = Ventana()
    login.ventana_inicio(titulo="Iniciar Sesion", texto="INICIAR SESIÓN")

    comp = Login(root=login)
    comp.add_contenido(titulo="INICIAR SESIÓN")

    

    login.mainloop()
