import tkinter
import time

radky = 20
sloupce = 20
pocetBunek = 8 # počet buněk na spawnutí
counter = 0 # pomocná proměnná na počítání buněk
matice = [[0 for _ in range(sloupce)] for _ in range(radky)] # matice na vykreslování
tahleGenerace = [[0 for _ in range(sloupce)] for _ in range(radky)] # matice buněk (současné generace)
pristiGenerace = [[0 for _ in range(sloupce)] for _ in range(radky)] # matice další generace

#event spuštěný při kliknutí
def click(event):
    global counter
    if (pocetBunek != counter):        
        # Výpočet šířky a výšky čtverečku na výpis
        sirka = c.winfo_width()/sloupce
        vyska = c.winfo_height()/radky
        # Výpočet kliknutého sloupce a řádku
        sl = int(event.x//sirka)
        rad = int(event.y//vyska)
        # nastavení buňky + vykreslení
        if not matice[rad][sl]:
            counter += 1
            matice[rad][sl] = c.create_rectangle(sl*sirka, rad*vyska, (sl+1)*sirka, (rad+1)*vyska, fill="black") # vykreslení čtverečku
            
            if pocetBunek == counter: # načtení matici buněk (jedniček)
                for i in range(len(matice)):
                    for j in range(len(matice)):
                        if matice[i][j] != 0:
                            tahleGenerace[i][j] = 1
                gameOfLife()
        # Případné vymazání
        else:
            c.delete(matice[rad][sl])
            counter-=1
            matice[rad][sl] = 0

def gameOfLife():    
    vykresli()
    dalsiGenerace()
    root.after(500, gameOfLife)
        
# vykreslování
def vykresli():
    for i in range(radky):
        for j in range(sloupce):
            # Výpočet šířky a výšky čtverečku na výpis
            sirka = c.winfo_width()/sloupce
            vyska = c.winfo_height()/radky
            if tahleGenerace[i][j] == 1:
                c.create_rectangle(j*sirka, i*vyska, (j+1)*sirka, (i+1)*vyska, fill="black")
            else: 
                
                c.create_rectangle(j*sirka, i*vyska, (j+1)*sirka, (i+1)*vyska, fill="white")

# nastavení nové generace  
def dalsiGenerace():
    for i in range(radky):
        for j in range(sloupce):
            pocetSousedu = spocitejSousedy(i, j)
            if (tahleGenerace[i][j] == 1 and pocetSousedu < 2):
                pristiGenerace[i][j] = 0
            elif (tahleGenerace[i][j] == 1 and pocetSousedu > 3):
                pristiGenerace[i][j] = 0
            elif (tahleGenerace[i][j] == 0 and pocetSousedu == 3):
                pristiGenerace[i][j] = 1
            else:
                pristiGenerace[i][j] = tahleGenerace[i][j]
        
    prevedNaAktualniGeneraci()

# přenastavení "příští" generace na nynější
def prevedNaAktualniGeneraci():
    for i in range(radky):
        for j in range(sloupce):
            tahleGenerace[i][j] = pristiGenerace[i][j]

# spočítání okolních sousedů buňky
def spocitejSousedy(x, y):
    ziviSousedi = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i < 0 or x + i >= radky): # mimo hranice
                continue
            if (y + j < 0 or y + j >= sloupce): # mimo hranice
                continue
            if (x + i == x and y + j == y): # stejná buňka
                continue
            ziviSousedi += tahleGenerace[x + i][y + j];
    
    return ziviSousedi

root = tkinter.Tk() # založení objektu Tkinter
c = tkinter.Canvas(root, width=500, height=500, borderwidth=1, background='white') # tvorba Canvasu
c.pack()
c.bind("<Button-1>", click)

root.mainloop()