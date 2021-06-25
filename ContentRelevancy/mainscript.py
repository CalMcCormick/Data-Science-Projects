# This is where everything will be put together in the end
import pandas as pd
from relevancycomparison import RelevancyScore

home_insurance_links = pd.read_csv(r"c:\Users\calmc\OneDrive\Desktop\Portfolio Projects\Data Science Projects\ContentRelevancy\home_insurance_links.csv")

links_from = home_insurance_links.LinkFrom

links_to = home_insurance_links.LinkTo


relevency_figures = pd.DataFrame(columns=["LinkFrom", "LinkTo", "Relevency Percent", "Relevancy Score", "Relevancy Multiplier"])

for i in range(len(links_to)):
    relevancy = RelevancyScore(links_from[i], links_to[i])
    percent = relevancy.relevancy_percent
    score = relevancy.relevancy_score
    multiplier = relevancy.relevancy_multiplier
    
    relevency_figures = relevency_figures.append({"LinkFrom":links_from[i], "LinkTo":links_to[i], "Relevency Percent":percent, "Relevancy Score":score, "Relevancy Multiplier":multiplier}, ignore_index=True)


relevency_figures.to_csv('home_insurance_relevancies_2.csv', index=False)

# print("\nLink 1:")
# print(f"\nPercentage Keywords Hit: {link1.relevancy_percent}%")
# print(f"Relevancy Score (Weighted): {link1.relevancy_score}")
# print(f"Relevancy Multiplier: {link1.relevancy_multiplier}\n")


# print("\nLink 2:")
# print(f"\nPercentage Keywords Hit: {link2.relevancy_percent}%")
# print(f"Relevancy Score (Weighted): {link2.relevancy_score}")
# print(f"Relevancy Multiplier: {link2.relevancy_multiplier}\n")

