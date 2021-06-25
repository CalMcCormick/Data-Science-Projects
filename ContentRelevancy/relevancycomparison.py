# Figuring out a score!
from nlpscript import SiteKeywordDict

class RelevancyScore():

    def __init__(self, from_url, to_url):

        self.from_url = from_url
        self.to_url = to_url
        
        self.link_from = SiteKeywordDict(self.from_url)
        self.link_to = SiteKeywordDict(self.to_url)
        self.target_keywords = len(self.link_to.dictionary)

        self.up_to_five, self.up_to_ten, self.up_to_fifteen, self.up_to_twenty, self.more_than_twenty = self.get_counts()
        self.up_five_m, self.up_ten_m, self.up_fifteen_m, self.up_twenty_m, self.mt_twenty_m = self.get_weightings()
        self.relevancy_score = self.get_relevancy_score()
        self.relevancy_percent = self.get_percentage_kws_hit()
        self.relevancy_multiplier = (self.relevancy_score/100) + 1

    def get_counts(self):

        # Counts of keyword mention frequency
        up_to_five = 0
        up_to_ten = 0
        up_to_fifteen = 0
        up_to_twenty = 0
        more_than_twenty = 0 

        # Simple for loop to do this
        for values in self.link_to.dictionary.values():

            if values <= 5:
                up_to_five += 1
            elif values <= 10:
                up_to_ten += 1
            elif values <= 15:
                up_to_fifteen += 1
            elif values <= 20:
                up_to_twenty += 1
            else:
                more_than_twenty += 1

        return up_to_five, up_to_ten, up_to_fifteen, up_to_twenty, more_than_twenty

    def get_weightings(self):

        up_five_m = 1 + (1 - round((self.up_to_five/self.target_keywords),2))
        up_ten_m = 1 + (1 - round((self.up_to_ten/self.target_keywords),2))
        up_fifteen_m = 1 + (1 - round((self.up_to_fifteen/self.target_keywords),2))
        up_twenty_m = 1 + (1 - round((self.up_to_twenty/self.target_keywords),2))
        mt_twenty_m = 1 + (1 - round((self.more_than_twenty/self.target_keywords),2))

        return up_five_m, up_ten_m, up_fifteen_m, up_twenty_m, mt_twenty_m

    def get_relevancy_score(self):

        # Lets make a relevancy score!
        score = 0
        for from_key in self.link_from.dictionary.keys():
            for to_key in self.link_to.dictionary.keys():
                if to_key == from_key:
                    if self.link_to.dictionary[from_key] <= 5:
                        score += self.up_five_m
                    elif self.link_to.dictionary[from_key] <= 10:
                        score += self.up_ten_m
                    elif self.link_to.dictionary[from_key] <= 15:
                        score += self.up_fifteen_m
                    elif self.link_to.dictionary[from_key] <= 20:
                        score += self.up_twenty_m
                    else:
                        score += self.mt_twenty_m

        score = round(score, 2)

        return score

    def get_percentage_kws_hit(self):

        # Getting percentage
        score = 0
        for from_key in self.link_from.dictionary.keys():
            for to_key in self.link_to.dictionary.keys():
                if to_key == from_key:
                    score += 1

        percent = round(((score/self.target_keywords)*100), 2)

        return percent

