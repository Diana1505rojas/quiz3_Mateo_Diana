from clases import *
import random

dicpac= {}
dicdat= {}
contador = -1

def main():
    print("/n SISTEMAS DE IMAGENES HOSPITALARIAS /n")
    while True:
        menu= int(input("""
            1. Ingresar paciente
            2. Ingresar imagen JPG o PNG
            3. Transformación de imagen DICOM
            4. Manipulación de imagen JPG o PNG
            5. Salir
            --> """))
        
        if menu == 1:
            url = input("Ingrese la ruta de la carpeta del paciente: ")
            ppal=principal()
            ppal.datos_dicom(url)
            nombre, id_paciente, edad = ppal.datos_paciente()
            id_paciente = int(input("Ingresa un ID de tres numeros:"))
            paciente = Paciente(nombre, edad, id_paciente)
            x=ppal.asignar_imagen(url, contador, paciente)
            

            dicpac[id_paciente] = paciente
            dicdat[id_paciente] = ppal
            print(f"El paciente ha sido ingresado con éxito con el ID: {id_paciente}")

        elif menu == 2:
            url = input(r"Ingrese la ruta de la imagen en formato JPG O PNG que desea subir: ")
            id = int(input("Ingresa un ID de tres letras:"))
            ppal=principal()
            y=ppal.im_png_jpg(url)
            dicdat[id] = ppal
            print("La imagen ha sido ingresada con exito con el siguiente ID: ", id)

        elif menu == 3:
            id = int(input("Ingrese el ID de la carpeta DICOM: "))
            ppal=principal()
            ppal.rotacion(id,dicdat,x)

        elif menu == 4:
            id = int(input("Ingrese el ID de la imagen JPG o PNG: "))
            trans = principal()
            trans.tranformacion(id,dicdat,y)

        elif menu == 5:
            print("Ha salido del sistema el sistema")
            break 


        else:
            print("Opcion no valida")
        
if __name__ == "__main__":
    main()


