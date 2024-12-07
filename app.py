from PySide6 import QtWidgets, QtCore
from movie import get_all_movies, Movie

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
        self.lbl_info = QtWidgets.QLabel("")
        self.lst_movie_list = QtWidgets.QListWidget()
        self.lst_movie_list.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection) # type: ignore
        self.btn_rem_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")
        
        self.layout.addWidget(self.lne_movie_title)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.lbl_info)
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
        self.lbl_info.setText("")
        movie_to_add = self.lne_movie_title.text()
        if not movie_to_add:
            self.lbl_info.setText("* Vous devez renseigner un titre de film.")
            return False
        
        movie = Movie(movie_to_add)
        result = movie.add_to_movies()
        if result:
            movie.add_to_movies()
        
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.ItemDataRole.UserRole, movie)
            self.lst_movie_list.addItem(lw_item)
            self.lbl_info.setText("* Le film a bien été ajouté.")
        else:
            self.lbl_info.setText("* Le film que vous voulez ajouter existe déjà.")
        
        self.lne_movie_title.setText("")
    
    def remove_movie(self):
        for selected_item in self.lst_movie_list.selectedItems():
            movie = selected_item.data(QtCore.Qt.ItemDataRole.UserRole)
            movie.remove_from_movies()
            self.lst_movie_list.takeItem(self.lst_movie_list.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec()