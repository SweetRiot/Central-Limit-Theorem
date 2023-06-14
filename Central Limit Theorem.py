#Experimentando con la teoría del límite central.
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt2
import random
import statistics
data=[]
medias=[]

# llenado de datos random a mi lista "data"
for i in range(10000):
    random_value=random.randint(1,100)
    data.append(random_value)
    #print("random value is: ", random_value)

# histograma de los datos random
#plt2.hist(data)
#plt2.show()
# creación de muestras
for i in range(1000):
    muestra = random.sample(data,70)
    medias.append(statistics.mean(muestra))

# Crear el histograma
plt.hist(medias,edgecolor='pink')
# Personalizar el histograma
plt.title('Histograma')
plt.xlabel('Medias de las muestras')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()
