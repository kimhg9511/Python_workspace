import sys
# 모듈 임포트
from PyQt5.QtWidgets import *
# QApplication 인스턴스 생성, app 변수에 바인딩
app = QApplication(sys.argv)
# label에 텍스트 입력 후 보여줌.
print(sys.argv)
label = QLabel("Hello PyQt")
label = QPushButton("Quit")
label.show()
# exec_() 메서드를 호출하여 이벤트 루프에 진입
app.exec_()