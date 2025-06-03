import random as rd

class TicTacToe:

    # 생성자
    def __init__(self):
        self.board = []

    # 게임판 초기화
    def createBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('*')
            self.board.append(row)

    # 첫 플레이어 선택
    def selectFirstPlayer(self):
        who = rd.randint(0, 1)
        if who == 0:
            return "X"
        else:
            return "O"

    # 기호 표시
    def markSpot(self, row, col, player):
        self.board[row][col] = player

    # 승리 상태 확인
    def isWin(self, player):
        n = len(self.board)

        # 행 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win == True:
                return win

        # 열 확인
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win == True:
                return win

        # 오른쪽 대각선 확인
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win == True:
            return win

        # 왼쪽 대각선 확인
        for i in range(n):
            if self.board[i][n - i - 1] != player:
                win = False
                break
        if win == True:
            return win

        return False

    # 잔여 빈칸 여부 확인
    def isBoardFull(self):
        for row in self.board:
            for item in row:
                if item == '*':
                    return False
        return True

    # 플레이어 변경
    def nextPlayer(self, player):
        if player == "O" :
            return "X"
        else:
            return "O"

    # 현재 게임판 상태 출력
    def showBoard(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # 게임 시작
    def start(self):

        # 새 게임판 생성
        self.createBoard()
        self.showBoard()

        # 첫 플레이어 선택
        player = self.selectFirstPlayer()
        # 게임 루프 시작
        while True:

            # 다음 플레이어 안내내
            if player == "X":
                print("컴퓨터 차례입니다.")
            else:
                print("사용자 차례입니다.")

            # 사용자 입력 대기, 컴퓨터일 경우 랜덤 위치 반환
            if player == "X":
                while True:
                    row, col = rd.randint(1, 3), rd.randint(1, 3)
                    if self.board[row - 1][col - 1] == "*":
                        break
                print("컴퓨터가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택하였습니다.\n")
            else:
                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요 : ").split()))
                print(f"사용자가 행 {row}, 열 {col} 을/를 선택하였습니다.")

            # row, col 입력값이 0, 0인 경우, 게임 종료
            if row == 0 and col == 0:
                break

            # 입력된 위치 표시
            self.markSpot(row - 1, col - 1, player)
            self.showBoard()

            # 현재 플레이어가 이겼는지 확인
            if self.isWin(player):
                if player == "X":
                    print("컴퓨터가 이겼습니다. 다시 도전하세요.")
                else:
                    print("사용자가 이겼습니다. 축하합니다.")
                break

            # 게임판 가득참 확인
            if self.isBoardFull():
                print("무승부입니다. 아깝습니다.")
                break

            # 플레이어 변경
            player = self.nextPlayer(player)

        # 최종 게임판 출력
        print()
        self.showBoard()

# 게임 생성
TTT = TicTacToe()

# 게임 시작
TTT.start()