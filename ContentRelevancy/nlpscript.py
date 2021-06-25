# This is a copy of getting the BoW dict for one site
# Turn this into a class please so it can just take a URL as an input
import requests as req
from bs4 import BeautifulSoup as bs
import html5lib
# going to need to preprocess the crap out of the text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from collections import Counter # create BoW dictionary

import nltk
# didn't know I needed these, but apparently I do.
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialising what I need to initialise
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

special_chars1 = ['.','’', '£', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-./'] 
special_chars2 = [':', ';', '<','=', '>', '?', '@', '[', '\\', ']', '^_', '`', '{', '|'] 
special_chars3 = ['}', '~', '1', '2', '3', '4', '5', '6', '7', '8','9', '^']
special_chars = special_chars1 + special_chars2 + special_chars3
stop_words = set(stopwords.words("english"))

class SiteKeywordDict:

    def __init__(self, url):
        self.url = url
        # Will make it do all the fun shit after initialising once done
        self.all_text = self.scrape_text()
        self.quiet_text = self.less_noise()
        self.lemmatized_text = self.clean_text()
        self.dictionary = self.create_dict()


    def scrape_text(self):

        url_text = req.get(self.url).text
        soup = bs(url_text, 'html5lib')
        # first extract all headers, just going to stick to H1's, H2's & H3's
        h1s = soup.find_all("h1")
        h2s = soup.find_all("h2")
        h3s = soup.find_all("h3")
        ps = soup.find_all("p")
        all_tags = [h1s, h2s, h3s, ps]

        all_text = ""
        for list in all_tags:
            for tag in list:
                all_text += tag.text.lower() + " "

        return all_text

    def less_noise(self):
        # TOKENIZE
        tokenised_text = word_tokenize(self.all_text)

        # TEXT PREPROCESSING
        # Noise removal
        text1 = [word for word in tokenised_text if word not in special_chars]
        text2 = [word for word in text1 if word not in special_chars]
        text3 = [word for word in text2 if word[0] not in special_chars]
        text4 = [word for word in text3 if (len(word) > 1)]
            
        return text4

    def clean_text(self):   
        # REMOVE STOPWORDS
        all_text_no_stops = [word for word in self.quiet_text if word not in stop_words]

        # NORMALISE TEXT
        stemmed_text = [stemmer.stem(token) for token in all_text_no_stops]
        
        # lEMMATISE - CAST EVERYTHING TO ROUTE FORM
        # Function for part of speech tagging
        def get_part_of_speech(word):

            probable_part_of_speech = wordnet.synsets(word)
            pos_counts = Counter()

            pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
            pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
            pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
            pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
            most_likely_part_of_speech = pos_counts.most_common(1)[0][0]

            return most_likely_part_of_speech

        lemmatized_text = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in stemmed_text]
        return lemmatized_text

    # Creating word count dictionary
    def create_dict(self):

        # This creates a word: wordcount dictionary
        word_count_dict = Counter(self.lemmatized_text)
        
        # getting rid of the words that are only mentioned once
        def remove_1s(dictionary):

            # Just adding everything to a new dict rather than editing the old one
            updated_dict = {}
            for word, count in dictionary.items():
                if count > 1:
                    updated_dict[word] = count 

            # Ordering from largest word count to smallest, just because it looks better
            updated_dict_2 = {k: v for k, v in reversed(sorted(updated_dict.items(), key=lambda item: item[1]))}

            return updated_dict_2

        return remove_1s(word_count_dict)

