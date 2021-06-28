# This is where everything will be put together in the end
import pandas as pd
from tkinter import *
from relevancycomparison import RelevancyScore
from tkinter import filedialog

# Allowing to just choose a file, rather than specifying the actual name
filename = filedialog.askopenfilename(initialdir='/', title='Select CSV File')
new_file_name = ".csv"

# Reading the CSV file 
insurance_links = pd.read_csv(filename)
# Seperating the links from and links to
links_from = insurance_links.LinkFrom
links_to = insurance_links.LinkTo

# Creating a dataframe template for the new CSV
relevency_figures = pd.DataFrame(columns=["LinkFrom", "LinkTo", "Relevency Percent", "Relevancy Score", "Relevancy Multiplier"])

# Looping through every URL and 
for i in range(len(links_to)):
    relevancy = RelevancyScore(links_from[i], links_to[i])
    percent = relevancy.relevancy_percent
    score = relevancy.relevancy_score
    multiplier = relevancy.relevancy_multiplier
    
    relevency_figures = relevency_figures.append({"LinkFrom":links_from[i], "LinkTo":links_to[i], "Relevency Percent":percent, "Relevancy Score":score, "Relevancy Multiplier":multiplier}, ignore_index=True)

# As I get better with GUI's I'll update this so you can select what you want to call it.
relevency_figures.to_csv(new_file_name, index=False)

