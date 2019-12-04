import streamlit as st
import pandas as pd
from IPython.display import Image #imagenes

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

        6 Ñoñadas

        """)    

    st.write("Vamos a ponerte un poco a prueba")
    
    options = st.multiselect(
        'Cuantos km hay entre Elche y Pamplona en linea recta?',
        (650, 730, 590, 742))

    video = open("video.mp4","rb")
    video_b = video.read()
    st.video(video_b)
                             
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
                             
                            
    img_9 = ("relax_1.png")
    imagen(img_9)
                             
                             
    st.header("Ñoñadas")
                             
                             
    st.write(""" Bueno cariño, espero que este viaje, pese a que a priori no estuviese
                en nuestra lista de deseos, lo disfrutes como todos aquellos de tus sueños que
                por suerte, me ha tocado vivir a tu lado. Esto suena tal vez un poco ñoñis, pero
                yo me muero de ganas de poder ver como todos y cada uno de tus sueños se hacen
                realidad a mi lado. Te doy las gracias por todo este tiempo, te doy las gracias
                por ser tu misma, por ser cariñosa, por preocuparte, por ser amable, una incre-
                ible compañera de vida. Me encanta ver todos y cada uno de los días tu sonrisa,
                tus ganas de crecer, tus ganas de viajar, tus ganas de amar, de cuidar al resto,
                sin importar el que te daran a cambio, en general, me encanta pasar los días a
                tu lado. Eres una persona que me llena, que me hace sentirme querido, y sobre
                todo, que me hace feliz. Yo espero, que año tras año, aun que te vayas haciendo
                vieja antes que yo, sientas y veas la vida con ojos similares a los mios, y pue-
                das, tener una opinio similar a la que yo tengo hacia tu persona. Con todo esto,
                no me enrollo más, cariño mio, te deseo, FELICES 23 años mi amor, te quiero mucho!!!""")

    st.title('TE QUIERO MUCHO, FELICES "· AÑAZOS')


if __name__ == "__main__":
    main()
