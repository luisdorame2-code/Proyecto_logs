import os
from datetime import datetime

#carpeta logs dentro del proyecto

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)


#nombre del archivo con fecha y hora
nombre = "logs_" + datetime.now().strftime("Y%m%d_%h%m%s") + ".txt"
ruta = os.p;ath.join(logs_dir, nombre)

#crear y escribir dentro del archivo
with open(ruta, "w") as f:
	f.write("Este log fue creado automaticamente\n")
print("Log creado en:", ruta)

