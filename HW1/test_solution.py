"""
八皇后问题 - 回溯法测试文件
运行此文件验证：是否找到92个解，且每个解都合法。
"""
import numpy as np
import copy
from board import Chessboard


class Game:
    def __init__(self, show=True):
        self.chessBoard = Chessboard(show)
        self.solves = []
        self.gameInit()

    def gameInit(self, show=True):
        self.Queen_setRow = [-1] * 8
        self.chessBoard.boardInit(False)

    # ========== 步骤1：冲突检测函数 ==========
    def is_valid(self, row, col):
        for i in range(row):
            if self.Queen_setRow[i] == col:
                return False
            if abs(row - i) == abs(col - self.Queen_setRow[i]):
                return False
        return True

    # ========== 步骤2：回溯搜索核心 ==========
    def run(self, row=0):
        if row == 8:
            self.solves.append(list(self.Queen_setRow))
            return
        for col in range(8):
            if self.is_valid(row, col):
                self.Queen_setRow[row] = col
                self.run(row + 1)
                self.Queen_setRow[row] = -1

    def showResults(self, result):
        self.chessBoard.boardInit(False)
        for i, item in enumerate(result):
            if item >= 0:
                self.chessBoard.setQueen(i, item, False)
        self.chessBoard.printChessboard(False)

    def get_results(self):
        self.run()
        return self.solves


# ========== 测试代码 ==========
if __name__ == '__main__':
    print("=" * 50)
    print("开始搜索八皇后所有解...")
    print("=" * 50)

    game = Game(show=False)
    solutions = game.get_results()

    print(f"\n找到解的数量：{len(solutions)}")
    print(f"八皇后问题的正确解数是 92")
    print(f"数量是否正确：{'✓ 正确！' if len(solutions) == 92 else '✗ 错误！'}")

    # 验证每个解的合法性
    print("\n正在逐一验证每个解是否合法...")
    all_valid = True
    for idx, sol in enumerate(solutions):
        # 检查：8个列号都在0~7且互不相同
        if len(set(sol)) != 8 or any(c < 0 or c > 7 for c in sol):
            print(f"  解 {idx}: {sol} —— 列号非法！")
            all_valid = False
            continue
        # 检查：任意两个皇后不在同一条斜线
        valid = True
        for i in range(8):
            for j in range(i + 1, 8):
                if abs(i - j) == abs(sol[i] - sol[j]):
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            print(f"  解 {idx}: {sol} —— 斜线冲突！")
            all_valid = False

    if all_valid:
        print("  ✓ 所有 92 个解均合法（无同列、无斜线冲突）！")

    # 展示前3个解
    print("\n" + "=" * 50)
    print("前 3 个解的棋盘展示：")
    print("=" * 50)
    for i in range(3):
        print(f"\n--- 解 {i + 1}: {solutions[i]} ---")
        game.showResults(solutions[i])

    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50)
