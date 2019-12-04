import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from IPython.display import Image #imagenes
import xlrd

def imagen(img):
	Image(url=img)
	st.image(img, width =500)


def main():

	st.title('FELIZ CUMPLEAÑOS MI AMOR')


	st.header("Información Util para tu cumpleaños")

	st.header("""
		1 Foto de nuestra reserva 

		2 Foto de los exteriores del hotel 
		
		3 Foto de la habitación
		
		4 Foto de la piscina y relax 
		""")

	video = open("video.mp4","rb").read()

	st.write("Vamos a ponerte un poco a prueba")

	options = st.multiselect(
			'Cuantos km hay entre Elche y Pamplona en linea recta?',
			('650', '730', '590', '742'))
	
	while options == "742":
		if options == "742":
			st.success('Has acertado, muy bien!!!')
			st.write("""Aqui tienes
				tu primer regalito:""" , options)
			st.video(video)
		else:
			st.write("Vuelve a intentarlo cariño")

		

	st.header("Y esta año, ¿A donde nos vamos?")

	st.write('Foto de nuestra reserva')



	img = ("Regalo/datos_reserva.png")
	imagen(img)



	img = ("Regalo/datos_reserva.png")
	imagen(img)


	img = ("Regalo/foto_hotel_1.png")
	imagen(img)


	img = ("Regalo/foto_hotel_2.png")
	imagen(img)


	img = ("Regalo/foto_hotel_3.png")
	imagen(img)

	img = ("Regalo/habitacion.png")
	imagen(img)


	img = ("Regalo/piscina_1.png")
	imagen(img)


	img = ("Regalo/piscina_2.png")
	imagen(img)



	img = ("Regalo/relax_1.png")
	imagen(img)


	img = ("Regalo/relax_1.png")
	imagen(img)



if __name__ == "__main__":
	main()




