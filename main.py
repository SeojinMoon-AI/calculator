import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit

class Calculator(QWidget):
    """
    간단한 계산기 GUI 애플리케이션입니다.
    이 클래스는 계산기의 메인 윈도우를 설정합니다.
    """
    def __init__(self):
        """
        Calculator 클래스의 생성자입니다.
        윈도우와 그 속성을 초기화합니다.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        메인 윈도우의 사용자 인터페이스를 초기화합니다.
        """
        # 윈도우 제목 설정
        self.setWindowTitle('계산기')

        # 윈도우 위치와 크기 설정 (x, y, width, height)
        self.setGeometry(300, 300, 400, 300)

        # 텍스트 에디트 생성
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True) # 읽기 전용으로 설정

        # "Message" 버튼 생성
        message_btn = QPushButton('Message', self)
        # 버튼 클릭 시 show_message 메서드 호출
        message_btn.clicked.connect(self.show_message)

        # "Clear" 버튼 생성
        clear_btn = QPushButton('Clear', self)
        # 버튼 클릭 시 clear_text 메서드 호출
        clear_btn.clicked.connect(self.clear_text)

        # 버튼들을 위한 수평 레이아웃
        hbox = QHBoxLayout()
        hbox.addWidget(message_btn)
        hbox.addWidget(clear_btn)

        # 전체 위젯을 배치할 수직 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(self.text_edit) # 텍스트 에디트를 레이아웃에 추가
        vbox.addLayout(hbox) # 버튼 레이아웃을 메인 레이아웃에 추가
        self.setLayout(vbox)

    def show_message(self):
        """버튼 클릭 시 텍스트 에디트에 텍스트를 추가합니다."""
        self.text_edit.append('Button Clicked')

    def clear_text(self):
        """Clear 버튼 클릭 시 텍스트 에디트의 내용을 지웁니다."""
        self.text_edit.clear()

def main():
    """
    애플리케이션을 실행하는 메인 함수입니다.
    """
    # QApplication 인스턴스 생성
    app = QApplication(sys.argv)

    # Calculator 클래스의 인스턴스 생성
    calc = Calculator()
    
    # 위젯을 화면에 보여줍니다.
    calc.show()

    # 애플리케이션의 이벤트 루프를 시작합니다.
    sys.exit(app.exec())


if __name__ == '__main__':
    main()