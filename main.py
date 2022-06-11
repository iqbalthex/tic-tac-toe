from tkinter import *

# syarat kemenangan
winn = (
  (1,2,3),
  (4,5,6),
  (7,8,9),
  (1,4,7),
  (2,5,8),
  (3,6,9),
  (1,5,9),
  (3,5,7)
)

class Sel:
  end = 0
  O = []
  X = []
  ox = 2
  sel = {}

  def __init__(self,baris,kolom,index):
    self.index = index
    Sel.sel[index] = Button(win, width=6, height=3, command=self.pencet)
    Sel.sel[index].grid(row=baris, column=kolom)

  def pencet(self):
    bg = "blue" if Sel.ox == 1 else "red"
    Sel.sel[self.index].configure(bg=bg,
      state='disabled') # menghindari pemilihan kotak berulang
    Sel.end += 1

    # semacam skor
    
    if Sel.ox == 1:
      Sel.O.append(int(self.index))
      Sel.O.sort()
      Sel.ox = 2
    else: 
      Sel.X.append(int(self.index))
      Sel.X.sort()
      Sel.ox = 1

    # mengecek adanya pemenang
    menn = None
    for a in range(3):
      for b in range(a+1,a+4):
        for c in range(b+1,b+4):
          try:
            x = (Sel.X[a],Sel.X[b],Sel.X[c])
            for i in winn:
              if x == i:
                menn = False
                Sel.menang = 1
                end(menn)
                break
          except: pass

          try:
            y = (Sel.O[a],Sel.O[b],Sel.O[c])
            for i in winn:
              if y == i:
                menn = False
                Sel.menang = 2
                end(menn)
                break
          except: pass
          if c == 4: break
        if b == 3: break

    if Sel.end == 9:
      if menn == True:
        end(True)
      else:
        end(False)


class MyLabel:
  def __init__(self,row,col,text,**kwargs):
    self.label = Label(win, font=20, text=text)
    self.label.grid(row=row,column=col)
    if kwargs:
      self.label.grid(columnspan=kwargs["columnspan"])

  def destroy(self):
    self.label.destroy()


# inisiasi permainan
def start():
  k = 0
  for i in range(1,4):
    for j in range(3):
      k += 1
      sel = Sel(i,j,str(k))

# akhir permainan
def end(draw):
  def reset():
    for i in Sel.sel:
      Sel.sel[i].destroy()

    over   .destroy()
    menang1.destroy()
    reset_ .destroy()
    Sel.end   = 0
    Sel.O     = []
    Sel.X     = []
    Sel.ox    = "X"
    Sel.sel = {}
    start()

  if draw and Sel.end == 9:
    Sel.menang = "tidak ada"

  for i in Sel.sel:
    Sel.sel[i].configure(state='disabled') # mengakhiri permainan

  over    = MyLabel(1,3,"Permainan berakhir")
  menang1 = MyLabel(2,3,f"Pemenang {Sel.menang}")
  reset_  = Button(win, font=20, text="Reset", command=reset)
  reset_ .grid(row=3, column=4)


if __name__ == "__main__":
  win = Tk()
  MyLabel(0,0,"Tic-tac-toe sederhana",columnspan=5)
  start()
  win.mainloop()