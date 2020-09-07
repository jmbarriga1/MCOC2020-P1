# MCOC2020-P1
# Entrega1 - Integración de ecuaciones diferenciales

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%201/graphic_balistica.png?raw=true)

# Entrega 2 - Primeras predicciones con la EDM básica del satélite

* La velocidad tangencial se encontro iterando y viendo en el grafico a continuación. Para que el satelite no toque la atmosfera la velocidad tangencial debe ser mayor a 6500 m/s, pero con velocidad tangencial 7000 m/s el satelite gira de manera estable.

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%202/Velocidad%20tangencial%20en%20la%20cual%20esta%20estable%20y%20no%20toca%20la%20orbita.png?raw=true)

* A continuación se puede cuanto demora el satelite para hacer dos orbitas, el cual es de 12700 segundos aproximadamente.

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%202/Distancia%20satelite%20respecto%20al%20tiempo%20para%20dos%20orbitas.png?raw=true)

* Tambien se puede apreciar  en el grafico de abajo la distancia que tiene el satelite, la atmosfera y la tierra, con respecto al tiempo. Cabe mencionar que el satelite en ningun momento entra a la atmosfera.

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%202/Distancia%20satelite%2C%20tierra%20y%20orbita%20respecto%20al%20tiempo.png?raw=true)

# Entrega3 - I/O de vectores de estado y predicciones usando la EDM básica

* La distancia a la cual se encuentra el satelite es de 1312339.378738718 metros.

# Entrega 4 - Estudio de convergencia Método de Euler

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* En el gráfico se puede apreciar que la solución analítica es prácticamente igual a la solución odeint, esto denota la precisión que tienen ambos métodos de solución.
* También se puede apreciar que para la solución euler mientras mayor es el numero de subdivisiones con la cual se analiza, mas precisa es.  Esta precisión se ve en el gráfico, ya que se acerca cada vez mas a los resultados de la solución odeint y la solución analítica.

# Entrega 5 - Mejoras al modelo y estudio de convergencia

* 1)

* Grafico posición x,y,z:

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* Grafico posición x,y,z con corrección J2 y J3:

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* 2)

![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* ¿Cuánto deriva eulerint de odeint en este caso al final del tiempo? Alfinal del tiempo eulerint de odeint deriva 3719,25 (Km).

* ¿Cuanto se demora odeint y eulerint respectivamente en producir los resultados? Odeint demora 0.6363 segundos y eulerint demora 1,9004 segundos.

* 3)

* ![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* ¿Cuantas subdivisiones hay que usar para que la predicción con eulerint al final del tiempo esté en menos de un 1% de error? Las subdivisiones que se hicieron para que la predicción sea cercana a un 1% fue de 500 subdivisiones el cual demoro un tiempo de 1893.62 en ejecutar ya que el computador demoraba mucho en hacer una subdivisión mayor.

* 4)

* ![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* ![alt text](https://github.com/jmbarriga1/MCOC2020-P1/blob/master/Entrega%204/graphic_entrega4.png?raw=true)

* ¿Cuánta deriva incurre al agregar las correcciones J2 y J3? ¿Cuanto se demora su código en correr? Con la correción J2 deriva 1752,18 (Km) con un tiempo de 0.5927 segundos y luego con la corrección J2 y J3 deriva 1748,56 (Km) con un tiempo de 0.5905.
