import streamlit as st 
import pandas as pd 
import streamlit.components.v1 as stc

import time 
timestr = time.strftime("%Y%m%d-%H%M%S")

html_temp = '''
		<div style = "background-color : #0A7F43;padding:10px;border-radius:30px">
		<h1 style = "color: white;text-align:center">Mini Excel Editor App</h1>
		</div>'''

html_temp1 = '''
		<div style = "background-color : #0A7F43;padding:10px;border-radius:30px">
		<h1 style = "color: white;text-align:center">Contact Form</h1>
		</div>'''

# set PAGE CONFIGURATION
page_config = {"page_title":"Excel like App","page_icon":"🔰","layout":"centered"}
st.set_page_config(**page_config,initial_sidebar_state = 'expanded')

#load csv
def load_data(data):
	return pd.read_csv(data)

def main():
	
	
	menu = ["Home","Contact"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		stc.html(html_temp)
		st.write("""
			### About App
			The app allows users to upload a CSV file, edit its data points, and then save and download the modified file.
			""")
		data_file = st.file_uploader("UPLOAD CSV FILE",type=["csv"])
		if data_file is not None:
			df = load_data(data_file)
			# saving form
			with st.form("editor_form"):
				edited_df = st.data_editor(df)
				save_button = st.form_submit_button("Save Data")
			

			if save_button:
				new_filename = f"{data_file.name}_{timestr}.csv"
				final_df = edited_df.to_csv()

				st.download_button(label = "Download data as CSV",data = final_df,file_name=new_filename,mime='text/csv')

	else:
		stc.html(html_temp1)
		st.header(":mailbox: Get In Touch With Me !")

		contact_form = '''
		<form action="https://formsubmit.co/anikethsurvi@gmail.com" method="POST">
	    	<input type="hidden" name="_captcha" value="false">
	    	<input type="text" name="name" placeholder="Your Name" required>
	    	<input type="gmail" name="gmail" placeholder="Enter Your Gmail" required>
	    	<textarea name = "message" placeholder="Your Message"></textarea>
	    	<button type="submit">Send</button>
		</form>'''

		st.markdown(contact_form,unsafe_allow_html=True)

		def local_css(file_name):
			with open(file_name) as f:
				st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

		local_css("C:/Users/hp/excel_streamlit/style.css")


if __name__ == '__main__':
	main()