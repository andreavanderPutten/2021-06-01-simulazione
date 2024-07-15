from database.DB_connect import DBConnect


from model.Gene import Gene


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGeni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
from genes_small.genes g """

        cursor.execute(query, )

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCorrelazioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  i.GeneID1 as gene1, i.GeneID2 as gene2, abs(i.Expression_Corr) as correlazione
from genes_small.interactions i 
where i.GeneID1 != i.GeneID2 
  
 """

        cursor.execute(query, )

        for row in cursor:
            result.append([row["gene1"],row["gene2"],row["correlazione"]])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getDD():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct g.GeneID as gene
from genes_small.genes g
where g.Essential = 'Essential'"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row["gene"])

        cursor.close()
        conn.close()
        return result

