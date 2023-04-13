# Jarníkův algoritmus za pomocí matice sousednosti
# časová složitost bude O(V^2), musí se pro každý vrchol projít všechny zbylé vrcholy

# počet vrcholů v grafu (vrcholy jsou značené od 0 do V-1, v tomhle případě do 4)
V = 5
# matice 5x5
# matice sousednosti reprezentující ohodnocený graf
G=[[0, 10, 20, 30, 5],
   [10, 0, 50, 42, 3],
   [20, 50, 0, 45, 1],
   [30, 42, 45, 0, 60],
   [5, 3, 1, 60, 0]]

inf = 1000000 # pomocná proměnná pro nekonečno 

# pole na zaznamenávání vybraných vrcholů
# vybrané bude zaznačeno jako true, jinak false
oznacene_vrcholy = [False, False, False, False, False]
pocet_hran = 0
# počet hran na minimální kostru bude vždy méně než V-1
# označíme nultý vrchol jako označený
oznacene_vrcholy[0] = True
print("Hrana | Váha")
# pro každý vrchol v grafu se prohledají sousední vrcholy
while (pocet_hran < V - 1):
    min = inf
    x = 0
    y = 0
    for i in range(V):
        # pokud je vrchol i označený, prochází se jeho sousední vrcholy j
        if oznacene_vrcholy[i]:
            for j in range(V): # kontrolujeme všechny vrcholy
                # Pokud je vrchol j neoznačený a 
                # existuje hrana mezi vrcholy i a j (G[i][j] je nenulové), 
                # vypočte se její váha (G[i][j]).
                if ((not oznacene_vrcholy[j]) and G[i][j]):
                    if min > G[i][j]: # je vzdálenost (ohodnocení hrany) menší než aktuálně vybrané minimum?
                        min = G[i][j] # nastav nové minimum
                        x = i 
                        y = j
    oznacene_vrcholy[y] = True 
    pocet_hran += 1 # počet hran přibyde
    print(f"{x}-{y} | {G[x][y]}") # tisk spojených vrcholů