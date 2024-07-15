import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
       geni = DAO.getDD()
       self._view.dd_gene.options =  list(map(lambda x: ft.dropdown.Option(x), geni))
    def handle_graph(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi : {self._model.grafoDetails()[0]},Numero di archi : {self._model.grafoDetails()[1]}"))
        self._view.update_page()
    def handle_geni_adiacenti(self,e):
        gene = self._view.dd_gene.value
        if gene == "" or gene == None :
            self._view.create_alert("Non hai scelto un elemento dal dropdown o non hai creato il grafo")
            self._view.update_page()
            return
        lista = self._model.geni_adiacenti(gene)
        self._view.txt_result.controls.append(ft.Text(f"Geni adiacenti a {gene}"))
        for elemento in lista :
            self._view.txt_result.controls.append(ft.Text(f"{elemento[1]} ---> {elemento[0]["weight"]}"))
        self._view.update_page()

    def handle_simulazione(self,e):
        pass
    def handle_path(self, e):
        pass