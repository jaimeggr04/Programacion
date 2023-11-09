"""
Un ciclista parte de una ciudad A a las HH horas, MM minutos
y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B
es de T segundos. Escribir un algoritmo que determine la hora de
llegada a la ciudad B.
"""

cityA = str(input("¿De que ciudad partes?: "))
HH = float(input("¿A que hora partes?: "))
MM = float(input("¿A que minutos partes?: "))
SS = float(input("¿A que segundos partes?: "))
cityB = str(input("¿Cual es su ciudad de destino?: "))
TS = float(input("¿Escribe en segundos cuanto tarda en llegar?: "))

# Pasamos de horas a segndos e igual con minutos
# Sumamos todos los segundos
sumT = HH*3600 + MM*60 + SS
sumF = sumT + TS

HH_arrival = sumF // 3600
MM_arrival = (sumF % 3600) // 60
SS_arrival = (sumF % 3600) % 60

print("LLegara a ", cityB, "a las", HH_arrival, ":", MM_arrival, ":", SS_arrival)
