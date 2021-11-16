from random import randint, choice
from captcha.image import ImageCaptcha
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class CaptchaCode(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('mainWindow.ui', None)
        self.ui.show()

        self.text = self.createText()
        self.createCaptchaCode()

        self.ui.check_btn.clicked.connect(self.check)
        self.ui.reset_btn.clicked.connect(self.reset)

    def createText(self):
        rand_range = randint(3, 6)
        text = ''
        for i in range(rand_range):
            rand_choice = choice([1, 2, 3])
            if rand_choice == 1:
                text += chr(randint(65, 90))
            elif rand_choice == 2:
                text += chr(randint(97, 122))
            elif rand_choice == 3:
                text += chr(randint(48, 57))
        return text
    
    def createCaptchaCode(self):
        cap = ImageCaptcha(width=280, height=90)
        data = cap.generate(self.text)
        cap.write(self.text, 'captcha.png')
        
        pixmap = QPixmap('captcha.png')
        self.ui.cap_label.setPixmap(pixmap)

    def check(self):
        user_text = self.ui.user_tb.text()
        mg_box = QMessageBox()
        mg_box.setWindowTitle('Message')
        if user_text == self.text:
            mg_box.setText('Correct !')
        elif user_text == '':
            mg_box.setWindowTitle('Warning !')
            mg_box.setText('You should type something first !')
        else:
            mg_box.setText('Wrong !')
        mg_box.exec()
        print(f'user text: {user_text}\ncaptcha text: {self.text}\n', '-'*10)

    def reset(self):
        self.text = self.createText()
        self.createCaptchaCode()

        self.ui.user_tb.setText('')

app = QApplication([])
window = CaptchaCode()
app.exec()