from pprint import pprint
from Extracting_Deep_Web import SearchableDatabase
import nltk as nltk
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
from nltk.chunk import tree2conlltags
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


class NLP:
    rangeValue_1 = "400000"
    rangeValue_2 = "600000"
    keyValue = "honda"
    rangeYear_1 = "2010"
    rangeYear_2 = "2018"
    companyName = "honda"
    list1 =[[''], ['']]
    temp_range = [""]
    temp_year = [""]
    temp_array = ['1', '2']

    def get_company_name(self):
        return self.companyName

    def check_year(self, mylist):

            if len(mylist) < 5:
                if mylist[0] == '1' or mylist[0] == '2':
                    return 0
                else:
                    return 1
            else:
                return 1


    def set_company_name(self, company_name):
         self.companyName = company_name

    def get_company_name(self):
        return self.companyName

    def getrangeValue_1(self):
        return self.rangeValue_1

    def setrangeValue_1(self, rangeValue1):
         self.rangeValue_1 = rangeValue1

    def setrangeValue_2(self, rangeValue2):
         self.rangeValue_2 = rangeValue2

    def getrangeValue_2(self):
        return self.rangeValue_2

    def getrangeYear_1(self):
        return self.rangeYear_1

    def setrangeYear_1(self, year_1):
         self.rangeYear_1 = year_1

    def getrangeYear_2(self):
        return self.rangeYear_2

    def setrangeYear_2(self, year_2):
         self.rangeYear_2 = year_2

    def keyValue(self):
        return self.keyValue

    def query_modification(self, sent):
        sent = nltk.word_tokenize(sent)
        sent = nltk.pos_tag(sent)
        return sent

    def check_bigger(self, temp_range):
        if temp_range[0] > temp_range[1]:
            temp_range[0], temp_range[1] = temp_range[1], temp_range[0]

        self.setrangeValue_1(temp_range[0])
        self.setrangeValue_2(temp_range[1])


    def apply_nlp2(self, searchabledatabase, query):
        #query = "old honda car  in lahore price range between 500000 to 600000 from 2015 to 2019 "
        #self.list1.clear()
        #self.temp_range.clear()
        #self.temp_year.clear()
        nlp = spacy.load("en_core_web_sm")
        p = word_tokenize(query)
        for n in p:
            doc = nlp(n)
            for entity in doc.ents:
                print(entity.text, entity.label_)
                self.list1[1].append(entity.text)
                self.list1[0].append(entity.label_)

        print(self.list1)
        self.temp_year.clear()
        self.temp_range.clear()
        self.set_company_name(self.search_company_name())
        print(self.get_company_name())
        find_range = self.search_range_value()
        if find_range == 2:
            self.temp_range.sort()
            self.setrangeValue_1(self.temp_range[0])
            self.setrangeValue_2(self.temp_range[1])
        elif find_range == 1:
            self.setrangeValue_1(self.temp_range[0])
            self.setrangeValue_2("")
        else:
            self.setrangeValue_1("")
            self.setrangeValue_2("")

        print(self.getrangeValue_1())
        print(self.getrangeValue_2())

        find_year = self.search_range_date()

        if find_year == 2:
            self.temp_year.sort()
            self.setrangeYear_1(self.temp_year[0])
            self.setrangeYear_2(self.temp_year[1])
        elif find_year == 1:
            self.setrangeYear_1(self.temp_year[0])
            self.setrangeYear_2("")
        else:
            self.setrangeYear_1("")
            self.setrangeYear_2("")

        self.update_value()
        print(self.getrangeYear_1())
        print(self.getrangeYear_2())
        self.list1[0].clear()
        self.list1[1].clear()
        self.temp_year.clear()
        self.temp_range.clear()




    def search_company_name(self):
        c_label = 0
        company_name = ""

        for j in range(len(self.list1[0])):
            if self.list1[0][j] == 'ORG':
             company_name = self.list1[1][j]
             c_label = 1

        if c_label == 0:
            return ""
        else:
            return company_name

    def search_range_value(self):
        c_label = 0

        for j in range(len(self.list1[0])):
            if self.list1[0][j] == 'CARDINAL':
                self.temp_range.append(self.list1[1][j])
                c_label += 1

        return c_label

    def search_range_date(self):
        c_label = 0

        for j in range(len(self.list1[0])):
            if self.list1[0][j] == 'DATE':
                self.temp_year.append(self.list1[1][j])
                c_label += 1

        return c_label

    def update_value(self):
        searchabledatabase = SearchableDatabase.SearchableDatabase.getInstance()
        searchabledatabase.setrangeValue_1(self.getrangeValue_1())
        searchabledatabase.setrangeValue_2(self.getrangeValue_2())
        searchabledatabase.setrangeYear_1(self.getrangeYear_1())
        searchabledatabase.setrangeYear_2(self.getrangeYear_2())
        searchabledatabase.set_company_name(self.get_company_name())























