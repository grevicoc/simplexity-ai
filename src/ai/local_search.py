import random
from time import time

from src.constant import GameConstant, ShapeConstant
from src.model import State
from utility import is_out

from typing import Tuple, List

class MoveConstant:
    RIGHT = "RIGHT"
    DRIGHT = "DIAGONAL_RIGHT"
    UP = "UP"
    DLEFT = "DIAGONAL_LEFT"
    LEFT = "LEFT"


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

    #untuk menentukan apakah bisa diisi atau tidak suatu kolom baris tertentu
    def is_fillable(self, state: State, col: int, row: int):
        return state.board.board[col][row-1 if row!=0 else row].shape!=ShapeConstant.BLANK

    #untuk menghitung value suatu kolom
    def calculateValue(self, state: State, col: int, row: int, resultList: List[Tuple[int, int, bool]], streakPlayer: int, streakEnemy: int, rotate: Tuple[str, bool], n_player: int):
        if not is_out(state.board,row,col) and self.is_blank(state,col,row):
            if self.is_fillable(state=state,col=col,row=row):
                if streakPlayer > streakEnemy:
                    resultList.append((col, streakPlayer , True))
                else:
                    resultList.append((col, streakEnemy , False))

        elif (not is_out(state.board,row,col)):
            current_piece = state.board.board[col][row]
            player = state.players[n_player]
            enemy = state.players[(n_player+1)%2]

            addPlayer = 1 if (player.shape==current_piece.shape or player.color==current_piece.color) else 0
            addEnemy = 1 if (enemy.shape==current_piece.shape or enemy.color==current_piece.color) else 0
            if (rotate[1]==True):
                self.calculateValue(state=state, col=col+1, row=row, resultList=resultList, streakPlayer=streakPlayer+addPlayer if addPlayer==1 else 0, streakEnemy=streakEnemy+addEnemy if addEnemy==1 else 0, rotate=(MoveConstant.RIGHT,False), n_player=n_player)    #kanan
                self.calculateValue(state=state, col=col+1, row=row-1, resultList=resultList, streakPlayer=streakPlayer+addPlayer if addPlayer==1 else 0, streakEnemy=streakEnemy+addEnemy if addEnemy==1 else 0, rotate=(MoveConstant.DRIGHT,False), n_player=n_player)    #diagonalkanan
                self.calculateValue(state=state, col=col, row=row-1, resultList=resultList, streakPlayer=streakPlayer+addPlayer if addPlayer==1 else 0, streakEnemy=streakEnemy+addEnemy if addEnemy==1 else 0, rotate=(MoveConstant.UP,False), n_player=n_player)    #atas
                self.calculateValue(state=state, col=col-1, row=row-1, resultList=resultList, streakPlayer=streakPlayer+addPlayer if addPlayer==1 else 0, streakEnemy=streakEnemy+addEnemy if addEnemy==1 else 0, rotate=(MoveConstant.DLEFT,False), n_player=n_player)    #diagonalkiri
                self.calculateValue(state=state, col=col-1, row=row, resultList=resultList, streakPlayer=streakPlayer+addPlayer if addPlayer==1 else 0, streakEnemy=streakEnemy+addEnemy if addEnemy==1 else 0, rotate=(MoveConstant.LEFT,False), n_player=n_player)    #kiri
            else:
                tempRow = row
                tempCol = col
                if (rotate[0]==MoveConstant.RIGHT):
                    tempCol+=1
                elif (rotate[0]==MoveConstant.DRIGHT):
                    tempCol+=1
                    tempRow-=1
                elif (rotate[0]==MoveConstant.UP):
                    tempRow-=1
                elif (rotate[0]==MoveConstant.DLEFT):
                    tempCol-=1
                    tempRow-=1
                elif (rotate[0]==MoveConstant.LEFT):
                    tempCol-=1
                self.calculateValue(state=state, col=tempCol, row=tempRow, resultList=resultList, streakPlayer=streakPlayer+addPlayer if addPlayer==1 else 0, streakEnemy=streakEnemy+addEnemy if addEnemy==1 else 0, rotate=(rotate[n_player],False),n_player=n_player)
                

    #untuk mengisi value tiap-tiap column
    def fillValueCells(self, state: State, n_player: int):
        #tuple 3 elemen, (column: int, value: int, is_attack: bool)
        listOfValue = []
        for i in range (state.board.col):
            current_piece = state.board.board[i][6]
            if (current_piece.shape!=ShapeConstant.BLANK):
                player = state.players[n_player]
                enemy = state.players[(n_player+1)%2]

                streakPlayer = 1 if (player.shape==current_piece.shape or player.color==current_piece.color) else 0
                streakEnemy = 1 if (enemy.shape==current_piece.shape or enemy.color==current_piece.color) else 0

                self.calculateValue(state=state,col=i,row=6,resultList=listOfValue, streakPlayer=streakPlayer, streakEnemy=streakEnemy, rotate=("ANYTHING",True), n_player=n_player)     
                return None
            else:
                listOfValue.append((i,0,False)) #nilai terendah, taro di paling belakang gapapa
    