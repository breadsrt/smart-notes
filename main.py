from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

text_edit = QTextEdit()

list_notes_lbl = QLabel("Список змін")
create_note_btn = QPushButton("Створити замітку")
delete_note_btn = QPushButton("Видалити замітку")
save_note_btn = QPushButton("Зберегти замітку")
tag_list_lbl = QLabel("Список тегів")
tegs_list = QListWidget()
search_line = QLineEdit("Ввід...")
add_tolist_btn = QPushButton("Додати до замітки")
del_from_list_btn = QPushButton("Відкріпити від замітки")
ser_by_teg_btn = QPushButton("Шукати по тегу")
notes_list = QListWidget()

main_line = QHBoxLayout()
main_line.addWidget(text_edit)

v1 = QVBoxLayout()
v1.addWidget(list_notes_lbl)
v1.addWidget(notes_list)
v1.addWidget(create_note_btn)
v1.addWidget(delete_note_btn)
v1.addWidget(save_note_btn)
v1.addWidget(tag_list_lbl)
v1.addWidget(tegs_list)
v1.addWidget(search_line)
v1.addWidget(add_tolist_btn)
v1.addWidget(del_from_list_btn)
v1.addWidget(ser_by_teg_btn)

main_line.addLayout(v1)


window.setLayout(main_line)
window.show()
app.exec()