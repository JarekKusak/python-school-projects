import numpy as np

# vývoj epidemie se řídí vztahem f(x) = e^(ax^2+bx+c)
A = np.array([[1**2, 1, 1],
              [2**2, 2, 1],
              [3**2, 3, 1],
              [4**2, 4, 1],
              [5**2, 5, 1],
              [6**2, 6, 1],
              [7**2, 7, 1]])
b = np.array([np.log(245), np.log(447), np.log(752), # převedeme do vztahu log(y) = ax^2+bx+c
              np.log(1167), np.log(1673), np.log(2214), np.log(2704)]) 
a = np.linalg.lstsq(A, b, rcond=None)[0] # najdeme parametry a,b,c -> vyšlo mi (-0,04, 0,72, 4,82)
print(a)
tyden = 1
predpoved_tyden = np.array([tyden**2, tyden, 1])
print(f"odhad pro {tyden} týden: "+ str(np.exp(a@predpoved_tyden)))
predchozi_predpoved = np.exp(a@predpoved_tyden)
print()
for i in range(2, 36):
    tyden = i
    predpoved_tyden = np.array([tyden**2, tyden, 1])
    predpoved = np.exp(a@predpoved_tyden)
    prirustek = predpoved - predchozi_predpoved
    predchozi_predpoved = predpoved
    print(f"odhad pro {tyden} týden: "+ str(predpoved)) # vrátíme e^(-0.04x^2 + 0.7206 + 4,82)
    print("přírůstek: ", prirustek)
    print()


