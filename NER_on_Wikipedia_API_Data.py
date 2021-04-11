#Wikipedia API
import wikipedia
import spacy_streamlit
import streamlit
import spacy
import en_core_web_sm
from bs4 import BeautifulSoup
import requests
import re

# Exrating data from given url using beautifulsoup
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    for script in soup(["script", "style", 'aside']):
        script.extract()  # Exracting data from url
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))  

def main():
    #Title of Application
    streamlit.title('NER on data from Wikipedia or URL in Streamlit App')

    #!python -m spacy download en_core_web_sm
    nlp = spacy.load("en_core_web_sm")
    menu = ['Wikipedia','URL'] 
    choice = streamlit.sidebar.selectbox('Menu',menu)
    if choice == 'Wikipedia':
        streamlit.subheader('Wikipedia')
        raw_docx = streamlit.text_input('Enter the Topic','wikipedia') # User can enter topic of own choice
        try:
            page= wikipedia.page(raw_docx) # Extract data from Wikipedia API
            article = nlp(page.summary) # NER operation on summary of given topic
            spacy_streamlit.visualize_ner(article, labels=nlp.get_pipe("ner").labels)
        except Exception as e:
            streamlit.write("Page id does not match any pages. Try another id!")
            streamlit.write("Please refer below suggestions")
            streamlit.write(SystemExit(e))

    else:
        streamlit.subheader('URL')
        raw_docx = streamlit.text_input('Enter the URL','https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news') # User can choose diffrent url for NER
        try:
            ny_bb=url_to_string(raw_docx) # Calling function to extract data from url
            article = nlp(ny_bb)
            spacy_streamlit.visualize_ner(article, labels=nlp.get_pipe("ner").labels)
        except:
            streamlit.write("Enter correct url")



if __name__ == '__main__':
	main()

