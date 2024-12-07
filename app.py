from PySide6 import QtWidgets, QtCore
from movie import get_all_movies

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self) # type: ignore
        self.lne_movie_title = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.lst_movie_list = QtWidgets.QListWidget()
        self.btn_rem_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        
        self.layout.addWidget(self.lne_movie_title)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.lst_movie_list)
        self.layout.addWidget(self.btn_rem_movie)
    
    def setup_connections(self):
        self.lne_movie_title.returnPressed.connect(self.add_movie)
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_rem_movie.clicked.connect(self.remove_movie)
    
    def populate_movies(self):
        movies = get_all_movies()
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.ItemDataRole.UserRole, movie)
            self.lst_movie_list.addItem(lw_item)
    
    def add_movie(self):
        print("On ajoute un film")
    
    def remove_movie(self):
        print("On supprime un film")


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()