# This is where everything will be put together in the end
import pandas as pd
from relevancycomparison import RelevancyScore

link_to_url_1 = "https://www.comparethemarket.com/home-insurance/"
link_from_url_1 = "https://www.lv.com/home-insurance"
lv_to_ctm = RelevancyScore(link_to_url_1, link_from_url_1)

print("\nLV TO CTM:")
print(f"\nPercentage Keywords Hit: {lv_to_ctm.relevancy_percent}%")
print(f"Relevancy Score (Weighted): {lv_to_ctm.relevancy_score}")
print(f"Relevancy Multiplier: {lv_to_ctm.relevancy_multiplier}\n")


link_from_url_2 = "https://www.moneysupermarket.com/home-insurance/"

msm_to_ctm = RelevancyScore(link_to_url_1, link_from_url_2)

print("\nMSM TO CTM:")
print(f"\nPercentage Keywords Hit: {msm_to_ctm.relevancy_percent}%")
print(f"Relevancy Score (Weighted): {msm_to_ctm.relevancy_score}")
print(f"Relevancy Multiplier: {msm_to_ctm.relevancy_multiplier}\n")