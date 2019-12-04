import streamlit as st
import pandas as pd
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from IPython.display import Image #imagenes
import xlrd

def main():

	st.title('TTF ANALYSIS')
	st.header("""1  Break-downs & Data frame cleaning:
		# DELETE THE UNNECESSARY COLUMNS 
		# TRANSFORM DATA TYPES
		# TAKE CARE OF NaN Values
		# CLEAN THE WHOLE DATA FRAME AND CHECK ERRORS ON IT
		# TAKE TTF VALUES BETWEEN 15-365 DAYS
		# PREPARE IT FOR FIRST VISUALIZATIONS""")

if __name__ == "__main__":
	main()


img = ("1*KljmJybQDj1mJAL-oS8VWQ.png")
Image(url=img)
st.image(img, width =500)

def clean_data():
	ttf = pd.read_excel("Offer Accept Report - 2017-2019.10.07.xlsx",
	                    header=2, parse_dates=['Req. Creation Date'])



	cols = ['Req. Organization Level 1', "Req. Primary Location Level 4",  # Exclude it temporary
	        'Req. Organization Level 3', 'Job Function',
	        'Requisition Type',"Req. Creation Date",
	        'Req. Current Status (Detail)', 'Req. Current Status (Parent)',
	        'Job Grade From', 'Job Grade To',"Req. First Sourcing Date",
	        'Req. No. Openings',
	        'Req. No. Openings Left To Fill', 'Req. Has Unlimited No. Openings',
	        'Req. Employee Status', 'Req. Job Shift', 'Req. Job Schedule',
	        'Req. Education Level', 'Req. Job Type', 'Req. User Group',
	        'Req. Bonus Currency', 'Req. Has Employee Referral Bonus',
	        'Relocation Package', 'Req. Pay Basis', 'Req. Minimum Salary',
	        'Req. Maximum Salary', 'Req. Hiring Manager Email',
	        'Req. Hiring Manager ID', 'Req. Recruiter Email',
	        'Req. Recruiter Department', 'Req. Recruiter Assistant Name',
	        'Requisition Type.1',
	        'Candidate Email', 'Candidate Full Name', 'Candidate ID', 'Source Of Hire Comment',
	        'Job Offer - Accepted Date',
	        'Job Offer - Actual Start Date', 'Cleared for OnBoarding Date', 'Project']

	ttf.drop(cols, axis=1, inplace=True)


	# Change the format of the date to : %Y-%m-%d

	ttf['Req. First Fully Approved Date'] = pd.to_datetime(
	    ttf['Req. First Fully Approved Date']).dt.strftime('%Y-%m-%d')

	ttf['Req. First Fully Approved Date'] = pd.to_datetime(
	    ttf['Req. First Fully Approved Date'], errors='coerce')


	# prevent from converting THE 0´S INTO NaN´S

	ttf.loc[ttf['Offer Job Grade'].isnull(), 'Offer Job Grade'] = "0"

	# In this data base there is problem, don´t know why it converts 1 to 0´s, so here, we change it back again:

	# ttf.loc[ttf['Offer Job Grade'].str.match("0") & (
	# ttf["SGL Group"].str.match("1 - 3")), "Offer Job Grade"] = 1


	# Exclude the values out of the range ["15-365"]
	ttf = ttf[(ttf["Time to Fill (Days)"] >= 16) &
	          (ttf["Time to Fill (Days)"] <= 365)]


	#ttf['Offer Job Grade'] = ttf['Offer Job Grade'].astype(float)

	ttf['Days from Offer accept to Cleared for Hire'] = ttf['Days from Offer accept to Cleared for Hire'].astype(
	    float)

	# Show me a preview
	ttf = ttf.dropna()
	st.dataframe(ttf.head())


	ttf["State"] = ttf["State"].str.replace(" ","")

	reviews = ttf['Recruiter'].str.cat(sep="")
	#function to split text into word
	tokens_r = word_tokenize(reviews)
	vocabulary_r = set(tokens_r)
	frequency_dist_r = nltk.FreqDist(tokens_r)
	#sorted(frequency_dist_r,key=frequency_dist_r.__getitem__, reverse=False)[0:50]

	#max_words=100, background_color="white"
	st.header("TOP RECRUITERS")

	wordcloud_r = WordCloud(width=1600, height=800, max_words=30).generate_from_frequencies(frequency_dist_r)
	plt.figure( figsize=(30,20), facecolor='k' )
	plt.imshow(wordcloud_r)
	plt.axis("off")
	plt.savefig('WordCloud.png')

	img = ("WordCloud.png")
	Image(url=img)
	st.image(img,width = 600)



	st.header("""2 Data Interpretation
		1) Region: APAC / EMEA / LATAM / NA --> WE´LL INDIVIDUALLY ANALYZE EACH!  
		2) Country --> graph for countries and a level of reqs since 2016   
		3) State --> Something similiar than above.
		4) Req. Organization Level 2 --> type of industry 
		5) Job Family --> job departments
		6) Req # --> ID
		7) Req.Title --> job possitio
		8) Justification --> new position VS. replacement
		9) Offer Job Grade         
		10) SGL Group --> Offer Job ranges             
		11) Req. Creation Date
		12) Hiring Manager
		13) Recruiter
		14) Time to Fill (Days)
		15) Req Aging Category
		16) INT/EXT
		17) Source Of Hire
		18) Days from Offer accept to Cleared for Hire"""
		)


if __name__ == "__main__":
	clean_data()


