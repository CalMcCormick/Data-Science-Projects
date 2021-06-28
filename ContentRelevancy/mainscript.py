# This is where everything will be put together in the end
import pandas as pd
from relevancycomparison import RelevancyScore

insurance_links = pd.read_csv("mar-may-first-fifty.csv")

links_from = insurance_links.LinkFrom

links_to = insurance_links.LinkTo


relevency_figures = pd.DataFrame(columns=["LinkFrom", "LinkTo", "Relevency Percent", "Relevancy Score", "Relevancy Multiplier"])

for i in range(len(links_to)):
    relevancy = RelevancyScore(links_from[i], links_to[i])
    percent = relevancy.relevancy_percent
    score = relevancy.relevancy_score
    multiplier = relevancy.relevancy_multiplier
    
    relevency_figures = relevency_figures.append({"LinkFrom":links_from[i], "LinkTo":links_to[i], "Relevency Percent":percent, "Relevancy Score":score, "Relevancy Multiplier":multiplier}, ignore_index=True)


relevency_figures.to_csv('mar-may-first-fifty-relevancies.csv', index=False)


