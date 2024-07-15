import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodi = []
        self.archi = []
        self.idMap = {}

    def creaGrafo(self):
        geni = DAO.getAllGeni()
        for gene in geni :
            if gene.Essential == "Essential" :
                self.nodi.append(gene.GeneID)
                self.idMap[gene.GeneID] = gene

        self.grafo.add_nodes_from(self.nodi)
        correlazioni = DAO.getAllCorrelazioni()
        for  correlazione in correlazioni :
            if correlazione[0] in self.nodi and correlazione[1] in self.nodi :
                peso = self.calcolaPeso(correlazione[0], correlazione[1], correlazione[2])
                self.archi.append([correlazione[0], correlazione[1],peso])
                self.grafo.add_edge(correlazione[0],correlazione[1],weight=peso)
    def getNodi(self):
        return self.nodi

    def geni_adiacenti(self,gene):
        vicini = self.grafo.edges(gene,data=True)
        lista_vicini = []
        for vicino in vicini :
            lista_vicini.append([vicino[2],vicino[1]])
        lista_vicini.sort()
        return lista_vicini


    def calcolaPeso(self,IDgene1,IDgene2,correlazione):
        gene1 = self.idMap[IDgene1]
        gene2 = self.idMap[IDgene2]
        peso = 0
        if gene1.Chromosome == gene2.Chromosome :
            peso = 2*correlazione
        else :
            peso = correlazione
        return peso


    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def trova_percorso(self,nodo_partenza):
        pass
    def ricorsione(self,parziale):
        pass
