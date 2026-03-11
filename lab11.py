#Oskar Górczyñski, 57785, 6/6


# Zad1
from re import L
import numpy as np
def zad1(n: int):
    A = np.ones((n,n), int)
    for i in range(n):
        for j in range(n):
            A[i,j]=(i+1)**j
    return A

print("Zadanie 1")
print(zad1(5))
print()
# Zad2
def zad2(n: int):
    A = np.ones((n,n), int)
    liczba=1
    for i in range(n):
        if(i%2==1):
            for j in range(n-1,-1,-1):
                A[i,j]=liczba
                liczba+=1
        if(i%2==0):
            for j in range(n):
                A[i,j]=liczba
                liczba+=1
    return A

print("Zadanie 2")
print(zad2(5))
print()

# Zad3
def zad3(n: int):
    A = np.zeros((n,n), int)
    liczba=1
    wiersz=n-1
    wiersz_gora=-1
    wiersz_dol=n
    kolumna=0
    kolumna_lewo=-1
    kolumna_prawo=n
    kierunek=1
    while liczba <= n**2:
        if kierunek==1:
            kierunek=2
            for i in range(wiersz_dol-1,wiersz_gora,-1):
                A[i,kolumna]=liczba
                liczba+=1
            kolumna_lewo+=1
            wiersz=wiersz_gora+1
        elif kierunek == 2:
            kierunek=3
            for j in range(kolumna_lewo+1,kolumna_prawo,1):
                A[wiersz,j]=liczba
                liczba+=1
            wiersz_gora+=1
            kolumna=kolumna_prawo-1
        elif kierunek == 3:
            kierunek=4
            for i in range(wiersz_gora+1,wiersz_dol,1):
                A[i,kolumna]=liczba
                liczba+=1
            kolumna_prawo-=1
            wiersz=wiersz_dol-1
        elif kierunek== 4:
            kierunek=1
            for j in range(kolumna_prawo-1,kolumna_lewo,-1):
                A[wiersz,j]=liczba
                liczba+=1
            wiersz_dol-=1
            kolumna=kolumna_lewo+1
    return A

print("Zadanie 3")
print(zad3(10))
print()

# Zad4
A = zad2(5)
A[A%5==0] = 0
A[A%3==0] = 0
print("Zadanie 4")
print(A)
print()

# Zad5
list={
    1: [2,4,6],
    2: [3],
    3: [],
    4: [],
    5: [4,5],
    6: [3]
}
def zad5(list: dict):
    n = len(list)
    A = np.zeros((n,n), int)
    for i in list.keys():
        for j in list[i]:
            A[i-1,j-1]=1
    return A

print("Zadanie 5")
print(zad5(list))
print()

# Zad6
def zad6(A: np.ndarray):
    det=0
    n= A.shape[0]
    for j in range(0,n,1):
        if j%2==0:
            det+=A[0,j]*determinant(A[1:,np.delete(np.arange(A.shape[1]),j)])
        else:
            det-=A[0,j]*determinant(A[1:,np.delete(np.arange(A.shape[1]),j)])
    
    return det

def determinant(A: np.ndarray):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Macierz musi byc kwadratowa")
    if A.shape[0] == 1:
        return A[0,0]
    if A.shape[0] == 2:
        return A[0,0]*A[1,1] - A[0,1]*A[1,0]

print("Zadanie 6")
A = np.array([[1,2,3],[4,7,6],[7,8,9]])
print(zad6(A))
print()
