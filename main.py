from kivy.lang import Builder
from kivymd.app import MDApp


class xo(MDApp):
    def build(self):
        self.title = "Tic Tac Toe "
        self.icon = "tic-tac-toe.ico"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("tic.kv")

    w = ""

    def looser(self):
        if self.root.ids.btn1.text != "" and \
                self.root.ids.btn2.text != "" and \
                self.root.ids.btn3.text != "" and \
                self.root.ids.btn4.text != "" and \
                self.root.ids.btn5.text != "" and \
                self.root.ids.btn6.text != "" and \
                self.root.ids.btn7.text != "" and \
                self.root.ids.btn8.text != "" and \
                self.root.ids.btn9.text != "":
            self.root.ids.scinfo.text = "TIE"

    def winner(self, a, b, c):
        self.w = a.text
        self.root.ids.scinfo.text = f"{a.text} wins!"

        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def logic(self):
        # horizontal
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.winner(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        elif self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text != "" and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.winner(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        elif self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text != "" and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.winner(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

        # diagonal
        elif self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text != "" and self.root.ids.btn5.text == self.root.ids.btn9.text:
            self.winner(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        elif self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text != "" and self.root.ids.btn5.text == self.root.ids.btn7.text:
            self.winner(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        # vertical
        elif self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.winner(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        elif self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn8.text:
            self.winner(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        elif self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text != "" and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.winner(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

        else:
            self.looser()

    t = 1

    def press(self, btn):
        if self.t == 1:
            btn.text = "X"
            btn.disabled = True
            btn.color = "orange"
            self.root.ids.scinfo.text = "O's turn"
            self.t = 0
        else:
            btn.text = "O"
            btn.disabled = True
            btn.color = "blue"
            self.root.ids.scinfo.text = "X's turn"
            self.t = 1
        self.logic()

    def restart(self):
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        self.root.ids.btn1.color = "gray"
        self.root.ids.btn2.color = "gray"
        self.root.ids.btn3.color = "gray"
        self.root.ids.btn4.color = "gray"
        self.root.ids.btn5.color = "gray"
        self.root.ids.btn6.color = "gray"
        self.root.ids.btn7.color = "gray"
        self.root.ids.btn8.color = "gray"
        self.root.ids.btn9.color = "gray"

        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        self.root.ids.scinfo.text = "X GOES FIRST!"
        self.t = 1


xo().run()
