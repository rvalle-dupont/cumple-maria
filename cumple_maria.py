import streamlit as st
import pandas as pd
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from IPython.display import Image #imagenes
import xlrd

def main():

	st.title('FELIZ CUMPLEAÑOS MI AMOR')



	st.header("Información Util para tu cumpleaños")

	st.header("""
		1 Foto de nuestra reserva 
		2 TRANSFORM DATA TYPES
		3 TAKE CARE OF NaN Values
		4 CLEAN THE WHOLE DATA FRAME AND CHECK ERRORS ON IT
		5 TAKE TTF VALUES BETWEEN 15-365 DAYS
		6 PREPARE IT FOR FIRST VISUALIZATIONS""")

	video = open("video.mp4","rb").read()

	if st.button('Quiero ver ese video, for sure!'):
    	st.video(vid_file)

	else:
		st.write('Pues Na')

	st.header("Y esta año, ¿A donde nos vamos?")

	st.write('Foto')

	img = ("Regalo/foto_prin.png")
	Image(url=img)
	st.image(img, width =500)



if __name__ == "__main__":
	main()




