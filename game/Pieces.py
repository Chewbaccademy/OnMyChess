from enum import Enum
from Board import Board, Square

class PieceType(Enum):
    KING = 1
    QUEEN = 2
    PAWN = 3
    BISHOP = 4
    CAVALIER = 5
    ROOK = 6

class Piece:
    
    def __init__(self, board:Board, square:Square, type:PieceType) -> None:
        self.board = board
        self.square = square
        self.type = type
    
    def can_move_specific_type(self, target_square:Square):
        return False
    
    
    def can_move(self, target_square:Square):
        return target_square in self.board \
            and target_square != self.square \
            and self.can_move_specific_type()
    
    def move(self, target_square:Square):
        if self.can_move(target_square=target_square):
            self.square = target_square
        else:
            raise ValueError(f"The piece {self} cannot move to the square : {target_square}")
    
    def __str__(self) -> str:
        return f"{self.type.name}:{self.square}"
        
        
class King(Piece):
    def __init__(self, square: Square) -> None:
        super().__init__(square, PieceType.KING)
        
    def can_move_specific_type(self, target_square: Square):
        return self.square.row - 1 <= target_square.row == self.square.row + 1 \
                and self.square.file - 1 <= target_square.file <= self.square.file + 1
             