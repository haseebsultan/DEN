class SearchableDatabase:
    __instance = None
    rangeValue_1 = "400000"
    rangeValue_2 = "600000"
    keyValue = "honda"
    rangeYear_1 = "2010"
    rangeYear_2 = "2018"
    companyName = "honda"

    @staticmethod
    def getInstance():
        """ Static access method. """
        if SearchableDatabase.__instance == None:
            SearchableDatabase()
        return SearchableDatabase.__instance

    def getpakwheels(self):
        return self.pakwheels

    def set_company_name(self, company_name):
         self.companyName = company_name

    def get_company_name(self):
        return self.companyName

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


    def __init__(self):
        """ Virtually private constructor. """
        if SearchableDatabase.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SearchableDatabase.__instance = self