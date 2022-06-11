from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import requests
from bs4 import BeautifulSoup
import bd

hrefs = []
list_regov = {}
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
           'Accept': '*/*'}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_count(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        e = soup.find('div', class_='pagination_block')
        finish = e.find('a', class_='pagination__finish').get('href')
        a = finish.find("page=")
        count = finish[a + 5:]
    except:
        count = 1
    return count


def get_content(html, reg):
    soup = BeautifulSoup(html, 'html.parser')
    e = soup.find('div', class_='articles articles_news-feed')
    for h in e.find_all('a', class_='articles-item__title'):
        if h.text.find("Пожар") or h.text.find("пожар"):
            hrefs.append({"Техногенный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Обрушен") or h.text.find("обрушен") or h.text.find("крушен") or h.text.find(
                "Крушен") or h.text.find("Паден") or h.text.find("паден"):
            hrefs.append({"Техногенный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Непогод") or h.text.find("непогод") or h.text.find("Шторм") or h.text.find("шторм"):
            hrefs.append({"Экологический": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Утон") or h.text.find("утон"):
            hrefs.append({"Социальный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("ДТП"):
            hrefs.append({"Транспортный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Спасен") or h.text.find("спасен") or h.text.find("Поиск") or h.text.find(
                "поиск") or h.text.find("Помощь") or h.text.find("помощь"):
            hrefs.append({"Социальный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Землетрясени") or h.text.find("землетрясени") or h.text.find("толч") or h.text.find(
                "Толч") or h.text.find("Сейсмо") or h.text.find("сейсмо"):
            hrefs.append({"Техногенный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Авари") or h.text.find("авари"):
            hrefs.append({"Техногенный": f'https://{reg}.mchs.gov.ru' + h.get('href')})

        elif h.text.find("Поджиг") or h.text.find("поджиг"):
            hrefs.append({"Техногенный": f'https://{reg}.mchs.gov.ru' + h.get('href')})


def get_datebase(html, type, reg_id,DB):
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find('div', class_='public__date').text
    Text1 = soup.find('div', class_='public__text')
    date = date[:len(date) - 7]
    d, m, y = date.split(' ')
    if m.find('янв') != -1:
        m = '01'
    elif m.find('фев') != -1:
        m = '02'
    elif m.find('мар') != -1:
        m = '03'
    elif m.find('апр') != -1:
        m = '04'
    elif m.find('ма') != -1:
        m = '05'
    elif m.find('июн') != -1:
        m = '06'
    elif m.find('июл') != -1:
        m = '07'
    elif m.find('авг') != -1:
        m = '08'
    elif m.find('сен') != -1:
        m = '09'
    elif m.find('окт') != -1:
        m = '10'
    elif m.find('ноя') != -1:
        m = '11'
    else:
        m = '12'
    if int(d) < 10:
        d = '0' + d
    date = y + "-" + m + "-" + d
    DB.add_info(type, reg_id, Text1.text, date)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.namedb = None
        self.setWindowTitle("MCHS")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("#centralwidget {background-image: url(1.jpg);}")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 29, 791, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 140, 801, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(25, 129, 247);\n "
                                         "border-radius: 8px;\n"
                                         "font: 16pt \"MS Shell Dlg 2\";")
        self.horizontalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(50, 300, 151, 41))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dateEdit.setFont(font)
        self.dateEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dateEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setDisplayFormat("")
        self.dateEdit.setDate(QtCore.QDate(2022, 6, 9))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(25, 129, 247);\n "
                                    "border-radius: 8px;\n"
                                    "font: 12pt \"MS Shell Dlg 2\";")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(590, 300, 151, 41))
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setDate(QtCore.QDate(2022, 6, 9))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(25, 129, 247);\n "
                                      "border-radius: 8px;\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 340, 221, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(25, 129, 247);\n "
                                      "border-radius: 8px;\n"
                                      "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 440, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(25, 129, 247);\n "
                                        "border-radius: 8px;\n"
                                        "font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 540, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(25, 129, 247);\n "
                                        "border-radius: 8px;\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Введите название региона"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Завершить"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_3.clicked.connect(self.Clean_Button)
        self.pushButton.clicked.connect(self.Add_reg)
        self.pushButton_2.clicked.connect(self.end)

    def Clean_Button(self):
        self.plainTextEdit.setPlainText("")

    def Add_reg(self):
        self.region = self.plainTextEdit.toPlainText()
        self.date1 = self.dateEdit.text()
        self.date2 = self.dateEdit_2.text()
        list_regov[self.region] = [self.date1, self.date2]
        self.plainTextEdit.setPlainText("")

    def end(self):

        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlainText("Загрузка")
        self.namedb, self.filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Создать")

        DB = bd.DB(f"{self.namedb}.db")
        DB.creat()
        for i in list_regov.keys():
            try:
                self.plainTextEdit.setPlainText("")
                self.plainTextEdit.setPlainText("Загрузка")
                date1 = list_regov[i][0]
                date2 = list_regov[i][1]
                region = i
                reg = DB.get_id_reg(region)
                if (reg == 50):
                    html = get_html(
                        f'https://50.mchs.gov.ru/deyatelnost/press-centr/vse-novosti?news_type=&news_date_from={date1}&news_date_to={date2}')
                    count = int(get_count(html.text))
                    for i in range(1, count + 1):
                        html = get_html(
                            f'https://50.mchs.gov.ru/deyatelnost/press-centr/vse-novosti?news_type=&news_date_from={date1}&news_date_to={date2}&page={i}')
                        get_content(html.text, reg)

                else:
                    if (reg < 10):
                        reg = '0' + str(reg)
                    html = get_html(
                        f'https://{reg}.mchs.gov.ru/deyatelnost/press-centr/vse_novosti?news_type=&news_date_from={date1}&news_date_to={date2}')
                    count = int(get_count(html.text))
                    for i in range(1, count):
                        html = get_html(
                            f'https://{reg}.mchs.gov.ru/deyatelnost/press-centr/vse_novosti?news_type=&news_date_from={date1}&news_date_to={date2}&page={i}')
                        get_content(html.text, reg)

                for i in hrefs:
                    for a in i.keys():
                        try:
                            html = get_html(i[a])
                            get_datebase(html.text, a, reg,DB)
                        except:
                            pass
            except:
                pass
        self.plainTextEdit.setPlainText("Готово")


def Application():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("2.jpg"))
    window = Window()

    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    Application()

