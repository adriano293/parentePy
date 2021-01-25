Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from guizero import App, Text, PushButton
import string
import numpy as np
import matplotlib.pyplot as plt

# apriamo il file in lettura
f = open(input(str(" Nome del file da aprire: ")))

# usiamo il metodo readlines 
# per ottenere una lista di righe del file

# stampiamo la prima riga
# print(f.readline()) 

# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []

# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe

for riga in f:
    valori = str(f.readline())  # converto in stringa la riga
    Nval = len(valori)          # conto il numero di caratteri
    valori = valori.strip('\n') # elimino i lterminatore di riga
    valori = valori.split(',')  # separo la stringa in due numeri
    valori = list(valori)       # converto in lista
    print(valori)
    coordX.append(int(valori[0])) # aggiungo la coordinata X
    coordY.append(int(valori[1])) # aggiungo la coordinata Y

f.close()  # chiudiamo il file

print ("X: ",coordX)
print ("Y: ",coordY)

# ordiniamo le liste
coordX.sort()
coordY.sort()

print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)

# stampo il tipo di dati delle coordinate
print(type(coordX))
print(type(coordY))

# ora sono pronte per essere usate anche nei grafici

plt.plot(coordX,coordY,)
plt.ylabel('some numbers')

def mostra_grafico():

    plt.show()

app = App(title="Grafico")

text = Text(app, text="Premi il pulsante per visualizzare il grafico")

button = PushButton(app, command=mostra_grafico)

app.display()
