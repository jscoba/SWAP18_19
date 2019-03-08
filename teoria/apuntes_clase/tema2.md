# SWAP - Servidores Web de Altas Prestaciones

## Tema 2 - Alta disponibilidad y escalabilidad

Índice de la sesión:

- Introducción
- Concepto de alta disponiilidad
- Concepto de escalabilidad
- Escalar un sitio web
- Conclusiones

### 2.1.- Introducción

Los dos conceptos teóricos más importantes de la asignatura son la **disponibilidad** (que nuestros servidores estén dando el servicio cuando el usuario nos visite) y la **escalabilidad** (que nuestras máquinas sean capaz de dar servicio a un número creciente de usuarios.)

La disponibilidad también tiene que ver con que nuestro servicio esté activo 24/7

Por muy potente que sea nuestra máquina (una sola) siempre va a haber un límite máximo de peticiones que no va a ser capaz de servir.

### 2.2.- Concepto de alta disponibilidad

Nuestro servicio debe estar activo el mayor tiempo posible. Cuando un sitio no está disponible se dice que está no disponible. Estos periodos de no disponibilidad pueden ser programados o no programados. Los periodos programados son las paradas técnicas de mantenimiento. Es un tiempo que deberá ser lo más corto posible pero que están bajo nuestro control.

Las paradas no programadas son las más peligrosas. Deberemos evitarlas lo máximo posible. Pueden ser por una avería hardware, un hacker que tira el sistema, un corte de luz o de red... Estas paradas se saben cuando empiezan pero no tenemos el control de cuanto van a durar.

Para medir la disponibilidad se sigue la siguiente fórmula (escala punto nueve)

$$ 100 - (\text{tiempoCaido} / \text{periodoTiempo}) * 100 $$

Así una caida de 1 hora en un día supone de un 95.83333% de disponibilidad. Una caida de 1 hora en una semana es un 99.404% de disponibilidad. El problema es cuando se produce esa parada

Lo ideal es llegar a un 100% de disponibilidad. Como esto es imposible, las empresas se conforman con un 99.99% de disponibilidad anual (una parada de 52 minutos al año).

Entrada de [blog](http://www.edgeblog.net/2007/in-search-of-five-9s/) que explica todos estos cálculos con más detenimiento.

Un problema en la medida es que los sistemas suelen ser mucho más complejos que una única máquina que está funcionando o caida. Hay un montón de elementos que pueden fallar de forma independiente (cada uno tiene una disponibilidad individual). Para obtener la disponibilidad del sistema completo se multiplican las disponibilidades individuales de los elementos. Si tenemos un sistema con dos servidores, cada uno con un 99% de disponibilidad. La disponibilidad del sistema completo es: $$ 99\%*99\% = 98.01\% $$ Es lógico que sea menor, debido a las distintas combinaciones de caidas que se pueden dar. La peor casuística posible es que las caidas vayan encadenadas (cuando se consigue levantar un servicio se cae el otro).

La forma de mejorar la disponibilidad es la redundancia. En un sistema completo podemos redundar los subsistemas con peor disponibilidad individual. Para calcular la nueva disponibilidad de eso componente usamos: $$ As = Ac_1 + ((1-Ac_1)*Ac_2) $$.

Ejercicio T2.1:

Sin replicar el Data Center

| Componente             | 1 elemento | 2 elementos | 3 elementos redundantes |
| ---------------------- | ---------- | ----------- | ----------------------- |
| Web                    | 85,0000%   | 97,7500%    | 99,6625000%             |
| Aplicacion             | 90,0000%   | 99,0000%    | 99,9000000%             |
| DB                     | 99,9000%   | 99,9999%    | 99,9999999%             |
| DNS                    | 98,0000%   | 99,9600%    | 99,9992000%             |
| Firewall               | 85,0000%   | 97,7500%    | 99,6625000%             |
| Switch                 | 99,0000%   | 99,9900%    | 99,9999000%             |
| Centro de datos        | 99,9900%   | 99,9900%    | 99,9900000%             |
| ISP                    | 95,0000%   | 99,7500%    | 99,9875000%             |
|                        |            |             |                         |
| Sistema                | 59,86697%  | 94,30193%   | 99,20360%               |
| Horas anuales De caida | 3516       | 499         | 70                      |

Aplicando la fórmula $$As = Ac_{n-1} + (1- Ac_{n-1})*Ac_n ​$$ aplicado a todos los elementos menos al centro de datos.

Al ser un cálculo teórico (basado además en estimaciones) no nos asegura nada, puede no fallar nunca o fallar más de lo que preveemos, ya que la disponibilidad no es más que eso, una previsión.

Para asegurar que todo nuestro sistema tenemos que tener en cuenta la disponibilidad de red, la de servidores y la de aplicaciones.

En cuanto a la disponibilidad de red tenemos que tener redundancia en conexiones, routers y servidores.

> Hace 3 o 4 años estuvo visitando el datacenter de Trevenque. Le comentaron que tenían 2 conexiones troncales de fibra de ADIF y luego tenían radioenlaces de ONO y Telefónica para así asegurar la conectividad de los servicios allí hospedados. Los dos enlaces de fibra van por acometidas distintas. 

Si tenemos suficiente dinero podemos tener duplicado cualquier elemento de los servidores. Facebook por ejemplo directamente pasó a diseñar sus propios servidores.

Un ejemplo de servidor de doble placa era el sistema de rover Curiosity [Enlace](http://bit.ly/15VxCBX) 

Además de redundancia hardware podemos tener esta redundancia mediante software (con balanceadores de carga por ejemplo).

En cuanto a disponibilidad de aplicaciones. Hay que hacer las aplicaciones redundantes y sin procesos que tengan un único punto de fallo. Además se debe intentar que no haya dependencias de módulos, o sistemas operativos muy específicos.

Ejercicio T2.2 para casa:

Buscar frameworks y librerías para diferentes lenguajes que permitan hacer aplicaciones altamente disponibles con relativa facilidad. Como ejemplo examina [PM2](https://github.com/Unitech/pm2) que sirve para administrar clústeres de NodeJS.

### 2.3.- Concepto de escalabilidad

La escalabilidad se refiere a la capacidad que tiene un sistema de adaptarse a cargas de trabajo crecientes. En sistemas web a un número creciente de peticiones. Si es capaz de adaptarse a la carga es adaptable.

Las empresas tienen dos opciones para hacer sus sitios escalables:

- Ampliación vertical: Ampliar las máquinas existentes (Mas CPU, RAM...)
- Ampliación horizontal: Añadir mas máquinas a una granja web.

[Graficas de escalabilidad ](http://bit.ly/XfBRoR) de Microsoft según escalabilidad vertical y horizontal.

Ejercicio T2.3: ¿Como analizar el nivel de carga de cada uno de los subsistemas en el servidor? Buscar herramientas y aprender a usarlas o recordarlas. 

### 2.4.- Escalar un sitio web

El nivel web se puede escalar balancearlo la carga, usando una máquina tampoco muy potente que distribuya la carga o usando un balanceador hardware (LocalDirector de Cisco, ServerIron de Foundry u otros). Hay varios algoritmos que se pueden usar para decidir que máquina servirá la petición.

En el nivel de aplicaciones se necesita que el software esté pensado para aprovechar el paralelismo y la transparencia de ubicación (no depender de una máquina en concreta para ejecutarse).

En el nivel de almacenamiento merece la pena tener varios niveles de almacenamiento:

- Discos duros internos para cada máquina (con el SO y lo básico para funcionar)
- Sistemas externos replicados con más seguridad conectados por NFS o LUSTRE donde se almacenen los datos

Ejercicio T2.4:

- Buscar ejemplos de balanceadores software y hardware.

- Buscar productos para servidores de aplicaciones

- Buscar productos para servidores de almacenamiento.

### 2.5.- Conclusiones

Conceptos clave: escalabilidad y alta disponibilidad.

### Resto de la sesión del 08-03-19

Artículo de 20 cuestiones a tener en cuenta al diseñar un sistema. Las más importantes:

- Documentarlo absolutamente todo
- Analizar y eliminar los puntos de fallos.
- Énfasis en la seguridad.
- Automatizar todo lo automatizable.
- Planificar todo antes de actuar.
- Mantener diferentes entornos (producción, desarrollo y backup)
- Usar software maduro
- Reutilizar la mayor parte de las configuraciones
- **Test everything**



Las diapositivas de este tema pueden encontrarse [aquí](https://es.slideshare.net/pacvslideshare/servidores-web-de-altas-prestaciones-tema-2).