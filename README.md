# Named Entity Recognition on scrapped data using wikipedia API
This Project is Hosted <a href="https://ner-wikipedia-data.herokuapp.com/">here</a>

Link: https://ner-wikipedia-data.herokuapp.com/

<img src="https://github.com/ApLife1827/NER_on_Wikipedia_API_Data/blob/main/readme-image.png">

## Installation
You need these dependencies:

    pip install streamlit
    pip install wikipedia
    pip install  spacy
    pip install spacy_streamlit
    pip install BeautifulSoup
    pip install html5lib

## Import libraries
    import wikipedia
    import spacy_streamlit
    import streamlit
    import spacy
    import en_core_web_sm
    from bs4 import BeautifulSoup
    import requests
    import re

## Title of Application
     streamlit.title('NER on data from Wikipedia or URL in Streamlit App')
     nlp = spacy.load("en_core_web_sm")
    
## Exrating data from given url using beautifulsoup
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib') 
    for script in soup(["script", "style", 'aside']):
        script.extract()  # Exracting data from url
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
    
## Created Menu for Wikipedia API and URL
    menu = ['Wikipedia','URL'] 
    choice = streamlit.sidebar.selectbox('Menu',menu)
    if choice == 'Wikipedia':
        streamlit.subheader('Wikipedia')
        raw_docx = streamlit.text_input('Enter the Topic','wikipedia') 
        # Exception Handling
        try:
            page= wikipedia.page(raw_docx) # Extract data from Wikipedia API
            article = nlp(page.summary) # NER operation on summary of given topic
            spacy_streamlit.visualize_ner(article, labels=nlp.get_pipe("ner").labels)
        except Exception as e:
            streamlit.write(SystemExit(e))
     else:
        streamlit.subheader('URL')
        raw_docx = streamlit.text_input('Enter the URL','https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?
        hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news') 
        try:
            ny_bb=url_to_string(raw_docx) # Calling function to extract data from url
            article = nlp(ny_bb)
            spacy_streamlit.visualize_ner(article, labels=nlp.get_pipe("ner").labels)
        except:
            streamlit.write("Enter correct url")

## Usage
    streamlit run NER_on_Wikipedia_API_Data.py
