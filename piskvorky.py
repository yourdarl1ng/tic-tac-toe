class Piskvorky:
    def __init__(self):
        self.field = ["-","-","-",
                      "-","-","-",
                      "-","-","-"]

    def getallpos(self):
        for pos in range(9):
            a = self.field[pos]
            print(a)
    def getfieldpos(self, pos):
        val = self.field[pos]
        return val
    def check_x_win(self):
        #horizontalne
        if self.field[0] == "x" and self.field[1] == "x" and self.field[2] == "x":
            return True
        if self.field[3] == "x" and self.field[4] == "x" and self.field[5] == "x":
            return True
        if self.field[6] == "x" and self.field[7] == "x" and self.field[8] == "x":
            return True
        #vertikalne(zlava)
        if self.field[0] == "x" and self.field[3] == "x" and self.field[6] == "x":
            return True
        if self.field[1] == "x" and self.field[4] == "x" and self.field[7] == "x":
            return True
        if self.field[2] == "x" and self.field[5] == "x" and self.field[8] == "x":
            return True
        #cez plochu do kriza
        if self.field[0] == "x" and self.field[4] == "x" and self.field[8] == "x":
            return True
        if self.field[2] == "x" and self.field[4] == "x" and self.field[6] == "x":
            return True
    def check_y_win(self):
        #horizontalne
        if self.field[0] == "y" and self.field[1] == "y" and self.field[2] == "y":
            return True
        if self.field[3] == "y" and self.field[4] == "y" and self.field[5] == "y":
            return True
        if self.field[6] == "y" and self.field[7] == "y" and self.field[8] == "y":
            return True
        #vertikalne(zlava)
        if self.field[0] == "y" and self.field[3] == "y" and self.field[6] == "y":
            return True
        if self.field[1] == "y" and self.field[4] == "y" and self.field[7] == "y":
            return True
        if self.field[2] == "y" and self.field[5] == "y" and self.field[8] == "y":
            return True
        #cez plochu do kriza
        if self.field[0] == "y" and self.field[4] == "y" and self.field[8] == "y":
            return True
        if self.field[2] == "y" and self.field[4] == "y" and self.field[6] == "y":
            return True
    def ai_move(self):
        print("move")
        if self.getfieldpos(4) == "-":
            self.field[4] = "y"
            print("center")
            return
 
        else:
            print("prediction")
            self.prediction()
            return

                
    def prediction(self):
        if self.field[4] == "x" and self.field[1] == "x":
            print("w")
            if self.field[7] == "-":
                print("w2")
                self.field[7] = "y"
                return
            else:
                pass
        elif self.field[4] == "x" and self.field[2] == "x":
            print("e")
            if self.field[6] == "-":
                print("e2")
                self.field[6] = "y"
                return
            else:
                pass
        
        elif self.field[4] == "x" and self.field[3] == "x":
            print("e")
            if self.field[5] == "-":
                print("e2")
                self.field[5] = "y"
                return
            else:
                pass
        elif self.field[4] == "y" and self.field[0] == "y":
            if self.field[8] == "-":
                self.field[8] = "y"
                print("win")
                return
            else:
                pass
        elif self.field[4] == "y" and self.field[1] == "y":
            if self.field[7] == "-":
                self.field[7] = "y"
                return
            else:
                pass
        elif self.field[4] == "y" and self.field[2] == "y":
            if self.field[6] == "-":
                self.field[6] = "y"
                return
            else:
                pass
        if self.field[0] == "x" and self.field[6] == "x":
            print("e")
            if self.field[4] == "-":
                print("e2")
                self.field[4] = "y"
                return
            else:
                pass
        for i in range(3):
            print(i)
            if self.field[i] == "x":
                print("cont")
                continue
            else:
                if self.field[i] == "-":
                    print("moved")
                    self.field[i] = "y"
                    return
                else:
                    continue
                
        for x in range(3, 6):
            print(x)
            if self.field[x] == "x":
                print("cont")
                continue
            else:
                if self.field[x] == "-":
                    print("moved")
                    self.field[x] = "y"
                    return
                else:
                    continue
        for t in range(6, 9):
            print(t)
            if self.field[t] == "x":
                print("cont")
                continue
            else:
                if self.field[t] == "-":
                    print("moved")
                    self.field[t] = "y"
                    return
                else:
                    continue
    def mainloop(self):
        print("ciselne znacenie ide zlava do prava, od nuly az po 8, prvy riadok ma 0 1 2")
        while True:
            
            print(f"0-2 |{self.field[0]}| |{self.field[1]}| |{self.field[2]}|")
            print(f"3-5 |{self.field[3]}| |{self.field[4]}| |{self.field[5]}|")
            print(f"6-8 |{self.field[6]}| |{self.field[7]}| |{self.field[8]}|")
            choice = input("choice->")
            if self.getfieldpos(int(choice)) == "-":
                self.field[int(choice)] = "x"
                self.ai_move()
            else:
                print("invalid move")
            if self.check_x_win():
                print("You win!")
                break
            if self.check_y_win():
                print("ai wins")
                break
            
p = Piskvorky()
p.mainloop()
        
