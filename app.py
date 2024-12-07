from PySide6 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self) # type: ignore
        self.lne_movie_title = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.lst_movie_list = QtWidgets.QListWidget()
        self.btn_del_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        
        self.layout.addWidget(self.lne_movie_title)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.lst_movie_list)
        self.layout.addWidget(self.btn_del_movie)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()