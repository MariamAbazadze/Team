import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from team_ui import Ui_MainWindow

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.show_player("გიორგი მამარდაშვილი"))
        self.ui.pushButton_2.clicked.connect(lambda: self.show_player("ოთარ კაკაბაძე"))
        self.ui.pushButton_3.clicked.connect(lambda: self.show_player("გურამ კაშია"))
        self.ui.pushButton_4.clicked.connect(lambda: self.show_player("ლუკა ლოჩოშვილი"))
        self.ui.pushButton_5.clicked.connect(lambda: self.show_player("ირაკლი აზაროვი"))
        self.ui.pushButton_6.clicked.connect(lambda: self.show_player("ოთარ კიტეიშვილი"))
        self.ui.pushButton_7.clicked.connect(lambda: self.show_player("გიორგი ქოჩორაშვილი"))
        self.ui.pushButton_8.clicked.connect(lambda: self.show_player("გიორგი ჩაკვეტაძე"))
        self.ui.pushButton_9.clicked.connect(lambda: self.show_player("გიორგი მიქაუტაძე"))
        self.ui.pushButton_10.clicked.connect(lambda: self.show_player("ბუდუ ზივზივაძე"))
        self.ui.pushButton_11.clicked.connect(lambda: self.show_player("ხვიჩა კვარაცხელია"))
        self.ui.players_label.setWordWrap(True)
        self.ui.players_label.setMinimumHeight(250)
        self.ui.players_label.setFixedWidth(300)
        self.ui.position_combo.addItems([
            "მეკარე", "მცველი", "ნახ.მცველი", "თავდამსხმელი"
        ])

        self.ui.position_combo.currentTextChanged.connect(self.show_players_by_position)


    def show_player(self, name):
        self.ui.players_label.setText(name)
    def show_players_by_position(self, position):
        players_by_position = {
            "მეკარე": ["გიორგი მამარდაშვილი"],
            "მცველი": ["ოთარ კაკაბაძე", "ლუკა ლოჩოშვილი", "გურამ კაშია", "ირაკლი აზაროვი"],
            "ნახ.მცველი": ["ოთარ კიტეიშვილი", "გიორგი ქოჩორაშვილი", "გიორგი ჩაკვეტაძე"],
            "თავდამსხმელი": ["ხვიჩა კვარაცხელია", "გიორგი მიქაუტაძე", "ბუდუ ზივზივაძე"]
        }
        players = players_by_position.get(position, [])
        if players:
            self.ui.players_label.setText("\n".join(players))
        else:
            self.ui.players_label.setText("მოთამაშე ვერ მოიძებნა.")

    def show_player_name(self, name):
        self.ui.players_label.setText(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())