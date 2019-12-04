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

	st.header("""Vamos por pasos:

		1 Video + audio para el recuerdo

		2 Foto de nuestra reserva 

		3 Foto de los exteriores del hotel 
		
		4 Foto de la habitación
		
		5 Foto de la piscina y relax 
		""")

	video = open("video.mp4","rb").read()

	st.write("Vamos a ponerte un poco a prueba")

	options = st.multiselect(
			'Cuantos km hay entre Elche y Pamplona en linea recta?',
			(650, 730, 590, 742))

	if options == 742:
		st.success('Has acertado, muy bien!!!')
		st.write("""Aqui tienes
				tu primer regalito:""" , options)

	if st.checkbox('Enseñame el video o que? '):

    	st.subheader('Video molon')

    	video = open("video.mp4","rb").read()

    	st.video(video)

	audio_file = open('myaudio.ogg', 'rb')
	audio_bytes = audio_file.read()

	st.audio(audio_bytes, format='audio/ogg')

	st.header("Y esta año, ¿A donde nos vamos?")

	st.write('Foto de nuestra reserva')

	st.header("Info de la resrva")

	img = ("datos_reserva.png")
	imagen(img)

	st.header("Fotos del Hotel")

	img_1 = ("foto_prin.png")
	imagen(img_1)


	img_2 = ("foto_hotel_1.png")
	imagen(img_2)


	img_3 = ("foto_hotel_2.png")
	imagen(img_3)


	img_4 = ("foto_hotel_3.png")
	imagen(img_4)

	st.header("Foto de nuestra habitacion")

	img_5 = ("habitacion.png")
	imagen(img_5)

	st.header("Piscina")

	img_6 = ("piscina_1.png")
	imagen(img_6)


	img_7 = ("piscina_2.png")
	imagen(img_7)

	st.header("Y un poquito de relax")

	img_8 = ("relax_1.png")
	imagen(img_8)


	img_8 = ("relax_1.png")
	imagen(img_9)



if __name__ == "__main__":
	main()




