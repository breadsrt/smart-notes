from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()


menu_btn = QPushButton("Меню")
image_lbl = QLabel("Картинка")
images_list = QListWidget()
dir_btn = QPushButton("Папка")
filter1 = QPushButton("фільтр1")
filter2 = QPushButton("фільтр2")
filter3 = QPushButton("фільтр3")
filter4 = QPushButton("фільтр4")
filter5 = QPushButton("фільтр5")

main_line = QHBoxLayout()

v1 = QVBoxLayout()
v1.addWidget(images_list)
v1.addWidget(dir_btn)
main_line.addLayout(v1)


v2 = QVBoxLayout()
v2.addWidget(image_lbl)
v2.addWidget(filter1)
v2.addWidget(filter2)
v2.addWidget(filter3)
v2.addWidget(filter4)
v2.addWidget(filter5)


window.setLayout(v2)
window.setLayout(v1)
window.setLayout(main_line)
window.show()
app.exec()
