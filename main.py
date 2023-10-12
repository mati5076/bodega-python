from login.empleado import Empleado
from login.producto import Producto
from login.bodega import Bodega
#permite al usuario ingresar con una cuenta para poder calcular precios y poder ver cuabnto stock de producto tiene
#el usuario es = matias y la contraseña = 1234
usuario = input("ingresa tú usuario :")
contraseña = input("ingresa tú contraseña : ")

matias = Empleado("Matias","20.588.550-1", "2000-10-04", usuario , contraseña)
matias.inicio_sesion()

supermercado = Bodega(120 , "calle Videla" , "Luis Gonzales")
print(f"la capacidad de productos :{supermercado.capacidad},queda : {supermercado.direccion},el jefe es :{supermercado.jefe_cargo}")


opcion = input("quieres ver los productos? ")

if opcion == "si":
    bebida = Producto("123124","Bebida Coca-cola","Bebidas","Ccoca-cola",1500,50,100)
    bebida.contador_bodega()
    bebida.calcular_precios()
else:
    print("cerraste sesion")
