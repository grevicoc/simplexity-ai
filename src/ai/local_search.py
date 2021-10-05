import random
from time import time

from src.constant import GameConstant, ShapeConstant
from src.model import State
from utility import is_out

from typing import Tuple, List


class LocalSearch:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        self.thinking_time = time() + thinking_time

        best_movement = (random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])) #minimax algorithm

        return None
    
    #untuk menentukan shapenya blank atau tidak
    def is_blank(self, state: State, col: int, row: int):
        return state.board.board[col][row].shape==ShapeConstant.BLANK

    #untuk 
    def calculateValue(self, state: State, col: int, row: int, resultList: List[Tuple[int, int, bool]]):
        resultList.append((col, 0, False) if is_out(state.board,row,col) and self.is_blank(state,col,row) else None)        #blm selesai

    #untuk mengisi value tiap-tiap column
    def fillValueCells(self, state: State):
        #tuple 3 elemen, (column: int, value: int, is_attack: bool)
        listOfValue = []
        for i in range (state.board.col):
            if (state.board.board[i][6].shape!=ShapeConstant.BLANK):
                self.calculateValue(state=state,col=i,row=6,resultList=listOfValue)     #blm selesai
                return None
            else:
                listOfValue.append((i,0,False)) #nilai terendah, taro di paling belakang gapapa

    

    