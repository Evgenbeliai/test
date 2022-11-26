from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QHBoxLayout, QVBoxLayout, QGroupBox, 
QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle
from random import randint


class Vopros():
    def __init__(self, question, p_o, n_o1, n_o2,n_o3):
        self.question = question
        self.p_o = p_o
        self.n_o1 = n_o1
        self.n_o2 = n_o2
        self.n_o3 = n_o3

q_list = list()

q_list.append(Vopros("Сколько лет","1211","12","12","12"))
q_list.append(Vopros("Сколько вес","131","13","13","13"))
q_list.append(Vopros("Сколько Рост","141","14","14","14"))

app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 



vopr = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask (q):
    shuffle(vopr)
    vopr[0].setText(q.p_o)
    vopr[1].setText(q.n_o1)
    vopr[2].setText(q.n_o2)
    vopr[3].setText(q.n_o3)

    lb_Question.setText(q.question)
    lb_Correct.setText(q.p_o)
    show_question()

def show_corekt(rezul):
    lb_Result.setText(rezul)
    show_result()


def Chek_answer():
    if vopr[0].isChecked():
        show_corekt("Молодец правильно")
        window.score +=1
        print("Количество правильных ответов", window.score, "из",len(q_list) )

    else:
        if vopr[1].isChecked() or vopr[2].isChecked() or vopr[3].isChecked():
            show_corekt("Sorry :(")

def next_q():
    window.num_q = window.num_q+1
    cur_question = randint(0, len(q_list) - 1)  
             
    q = q_list[cur_question] # взяли вопрос
    ask(q) # спросили




def start():
    if 'Ответить' == btn_OK.text():
        Chek_answer()
    else:
        next_q()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.num_q = -1

window.score = 0

btn_OK.clicked.connect(start) 
next_q()
window.show()
app.exec()
