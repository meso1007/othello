from numpy import zeros, where, float32

class othello:
    white = 1.
    black = -1.
    empty = 0.
    edge = 8          

    
    def __init__(self):
        self.board = zeros(self.edge**2, dtype=float32)    
        self.board[27] = self.board[36] = self.white           
        self.board[28] = self.board[35] = self.black     
        self.turn = True                          
        self.available = []                       

    
    def over(self, s, ex=True):
        s = int(s)
        start = s
        my_color = self.white if self.turn else self.black      
        flag = False               
        for i in range(-1, 2):
            for j in range(-1, 2):
                v = self.edge * i + j       
                if v == 0:
                    continue
                s = start
                for k in range(self.edge - 1):
                    s += v                         
                    if (s < 0 or s > self.edge**2 - 1 or self.board[s] == self.empty):   
                        break
                    if self.board[s] == my_color:                        
                        if k > 0:                                               
                            if ex:          
                                self.board[start + v: s : v] *= -1      
                            flag = True                                    
                        break
                    if (((s % self.edge == 0 or s % self.edge == self.edge - 1) and abs(v) != self.edge)
                        or ((s // self.edge == 0 or s // self.edge == self.edge - 1) and abs(v) != 1)):
                        break
        if flag and ex:                   
            self.board[start] = my_color
        return flag

    
    def judge(self):
        n_white = len(where(self.board == self.white)[0])      
        n_black = len(where(self.board == self.black)[0])      
        print("\n", "黒 >> ", n_black, "   白 >> ", n_white, "\n")     
        if n_white < n_black:                   
            print("あなた(黒)の勝ち")
        elif n_black < n_white:
            print("CPU（白）の勝ち")
        else:
            print("引き分け")

    
    def update(self, end=False):
        self.turn ^= True
        self.available = []                                             
        if self.board[i] == self.empty and self.over(i, ex=False):
                self.available.append(i)
        if len(self.available) == 0:           
                return False if end else self.master(end=True)           
        self._input()
        return True

    def _input(self):
        while True:
            msg = "白のターン" if self.turn else "黒のターン"         
            x, y = map(int, input(msg + "  縦 横 >> ").split())
            if 8 * x + y in self.available:                     
                self.over(8 * x + y)                            
                break
            print("---Invalid Position---")                    

    
    def draw(self):
        edge = self.edge
        print("\n    0  1  2  3  4  5  6  7")
        for i in range(edge):
            temp = []
            temp.append(str(int(i)))
            for el in self.board[edge * i:edge * (i + 1)]:
                if el == self.white:
                    temp.append("○")
                elif el == self.black:
                    temp.append("●")
                else:
                    temp.append("＋")
            print(" ".join(temp))            


def main():
    s = othello()               
    flag = True                  
    while flag:
        s.draw()                 
        flag = s.update()     
    s.judge()                    

if __name__ == "__main__":
    main()
