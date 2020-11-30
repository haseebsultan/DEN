from Query_Modification import NLP
class user_query:

    query = "null"


    def getUserQuery(self):
        return self.query

    def setUserQuery(self, query):
        self.query = query

    def getNLP(self):
        nlp =NLP.NLP()
        return nlp
