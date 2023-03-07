

class Square:
    
    def __init__(self, row:int, file:int) -> None:
        if 0 <= row <= 7:
            self.row = row
        else:
            raise ValueError("The row of the square must be between '1' and '8'")
        
        if 0 <= file <= 7:
            self.file = file
        else:
            raise ValueError("The file of the square must be between 'a' and 'h'")
        
    def get_row(self) -> int:
        return self.row + 1
    
    def get_file(self) -> int:
        files = "abcdefgh"
        return files[self.file]
        
    def __str__(self) -> str:
        return f"{self.get_file()}{self.get_row()}"
        
class Board:
    def __init__(self) -> None:
        self.squares_list = []
        for row in range(8):
            for file in range(8):
                self.squares_list.append(Square(row, file))
                
    def get_squares(self) -> list[Square]:
        return self.squares_list
    
    def __contains__(self, square:Square):
        return square in self.squares_list
    
    def __str__(self) -> str:
        return str([str(x) for x in self.get_squares()])