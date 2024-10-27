import os
from PIL import Image
from PIL.ImageQt import QImage, QPixmap
from PyQt6.QtWidgets import *


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap
class PhotoManager:
    def __init__(self):
        self.photo = None
        self.folder = None
        self.filename = None

    def load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)



    def show_image(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)

app = QApplication([])
window = QWidget()
app.setStyleSheet("""
        QWidget{
            background: 4f4e4e;
        }
        QPushButton
        {
            background-color: #6a23ba;
            border-style: groove;
            border-width: 5px;
            border-color: blue;
            border-radius: 7px;
        }
    """)

menu_btn = QPushButton("Меню")
image_lbl = QLabel("Картинка")
list_widget = QListWidget()
dir_btn = QPushButton("Папка")
filter1 = QPushButton("фільтр1")
filter2 = QPushButton("фільтр2")
filter3 = QPushButton("фільтр3")
filter4 = QPushButton("фільтр4")
filter5 = QPushButton("фільтр5")

main_line = QHBoxLayout()
v1 = QVBoxLayout()
v1.addWidget(dir_btn)
v1.addWidget(list_widget)
main_line.addLayout(v1)


v2 = QVBoxLayout()
v2.addWidget(image_lbl)
h1 = QHBoxLayout()
h1.addWidget(filter1)
h1.addWidget(filter2)
h1.addWidget(filter3)
h1.addWidget(filter4)
h1.addWidget(filter5)

photo_manager = PhotoManager()

def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(photo_manager.folder)
    list_widget.clear()
    list_widget.addItems(files)


def show_chosen_image():
    photo_manager.filename = list_widget.currentItem().text()
    photo_manager.load()
    photo_manager.show_image(image_lbl)


main_line.addLayout(v2)
v2.addLayout(h1)

list_widget.currentRowChanged.connect(show_chosen_image)
dir_btn.clicked.connect(open_folder)
window.setLayout(main_line)
window.show()
app.exec()


