import nilearn.image
import nilearn.plotting
import pydicom
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import dicom2nifti
import nilearn

class Paciente:
    def __init__(self, nombre, edad, id):
        self.__nombre = nombre
        self.__edad = edad
        self.__id = id
        self.__imagen = []

    def set_imagen(self, imagen):
            self.__imagen.append(imagen)

class principal:
    def __init__(self):
        self.__datos = []

    def set_datos(self, archivos):
        self.__datos.append(archivos)

    def get_datos(self):
        return self.__datos

    def im_png_jpg(self,url):
        img= cv2.imread(url)
        self.__datos.append(img)
        nombreimg=url.split('\\')[-1].split(".")[0]
        return nombreimg

    def datos_paciente(self):
        nombre = self.__datos[0].PatientName
        id = self.__datos[0].PatientID
        try:
            edad = self.__datos[0][ 0x0010 , 0x1010 ].value
        except:
            edad = 'No disponible'
        return nombre, id, edad
    
    def datos_dicom(self, url):
        archivos = os.listdir(url)
        for archivo in archivos:
            if archivo.endswith('.dcm'): 
                urldicom = os.path.join(url, archivo)
                dicom = pydicom.dcmread(urldicom) 
                self.__datos.append(dicom)

    def asignar_imagen(self, url, contador, paciente):

        nif= r"C:\Users\Sofia Rojas\Documents\quiz3_Mateo_Diana\nifti"
        dicom2nifti.convert_directory(url, nif)
        contador +=1
        datosnifti = os.listdir(nif)
        imagenes = os.path.join(nif,datosnifti[contador])
        imagen = nilearn.image.load_img(imagenes)
        paciente.set_imagen(imagen)
        nombreimg=url.split('\\')[-1].split(".")[0]
        return nombreimg

    def rotacion(self,id,dic,x):
        for i in dic.keys():
            if id== i:
                datos=dic[id]
                dato= datos.get_datos()
                eleccion=int(input(f"Selecciona la imagen que desea rotar (0-{len(dato)}): "))
                imagen=dato[eleccion].pixel_array
                angulo=int(input("Ingresa el angulo al que lo deseas rotar(90°,180°,270°): "))
                imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
                matriz_rotacion= cv2.getRotationMatrix2D(((np.shape(imagen)[0])/2,(np.shape(imagen)[1])/2),angulo,1)
                mgr=cv2.warpAffine(imagen,matriz_rotacion,(np.shape(imagen)[0],np.shape(imagen)[1]))
                cv2.imwrite(r"C:\Users\Sofia Rojas\Documents\quiz3_Mateo_Diana\rotaciones\imagenrotada_%s.jpg" %x,mgr)
                plt.subplot(1, 2, 1)
                plt.imshow(mgr)
                plt.title("Imagen rotada")
                plt.axis('off')
                plt.subplot(1, 2, 2)
                plt.imshow(imagen)
                plt.title("Imagen original")
                plt.axis('off')
                plt.show()
    
    def tranformacion(self,id,dic,y):
        for i in dic.keys():
            if id== i:
                datos=dic[id]
                dato= datos.get_datos()[0]
                imagenori = cv2.cvtColor(dato, cv2.COLOR_BGR2RGB)
                eje_x=int(input("Ingresa el valor del kernel en x: "))
                eje_y=int(input("Ingresa el valor del kernel en y: "))
                kernel = np.ones((eje_x,eje_y),np.uint8)
                Umbral=int(input("Ingresa el valor del umbral: "))
                umb,imagenbin = cv2.threshold(imagenori,Umbral,255,cv2.THRESH_BINARY)
                imagenmorph = cv2.morphologyEx(imagenbin, cv2.MORPH_CLOSE, kernel,iterations=1)
                cv2.putText(imagenmorph, f"Imagen binarizada con {umb} y kernel {eje_x}x{eje_y}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.imwrite(r"C:\Users\Sofia Rojas\Documents\quiz3_Mateo_Diana\transformaciones\transformacion_%s.jpg" %y,imagenmorph)
                plt.subplot(1, 2, 1)
                plt.imshow(imagenmorph)
                plt.title("Imagen transformada")
                plt.axis('off')
                plt.subplot(1, 2, 2)
                plt.imshow(imagenori)
                plt.title("Imagen original")
                plt.axis('off')
                plt.show()  
    

    