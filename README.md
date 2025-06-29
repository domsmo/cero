Código funcional que responde a las solicitudes realizadas por el cliente. Cuenta con 4 funciones:

read_file(): Sirve para leer los archivos de entrada .json que contiene el listado de citas y los requerimientos del cliente. Se decidió utilizar archivos .json por el orden que se obtiene de los mismos, con su formato de clave, valor.

filtro_dias(): Se decidió crear para obtener un primer filtro de datos, el cual elimina las citas que no correspondería contactar debido a la condición "días antes" que se compara con la fecha actual y la fecha de la cita. 

edad_paciente(): Se utiliza para crear una nueva categoría llamada "grupo etario" que sirve para filtrar las citas de pediatría (es un poco redundante pero nunca está de más corroborar que los pacientes son niños). Se considera que la función está demás porque podría ser uno de los campos de entrada. Se elimina en un futuro.

filtrado_citas(): Función principal. Toma el subconjunto de datos creado por filtro_dias() para estudiar las condiciones que podría tener la cita, comparandolo con las "reglas" de los requerimientos del cliente. En caso de que exista condiciones, se procede a ver si existen exclusiones filtrándolas. Si no existen condiciones, se detiene el loop para no guardar la cita. 

Problemas que enfrenté:

En algún momento existió un campo llamado "estado" que consideraba el estado de confirmación: confirmada, cancelada, pendiente. Al agregar la exclusión de "estado": "cancelada" no se eliminaban las citas que, contenían condiciones pero no exclusiones. La solución era agregarle a todas las reglas la exclusión de "estado": "cancelada", pero como no era un campo que explícitamente se tenía, se decidió eliminar. 

Suposiciones:
- Con el requerimiento de pediatría no se especificaba cuántos días antes requería confirmar, se dejó en 1 arbitrariamente. 
- Para el caso de cardiología, se le avisa al paciente 0, 2 y 5 días antes (separadas por reglas distintas).
- Dra. Gomez es cardiologa (se utilizó para ver si a pesar de haber reglas con condiciones en cardiología, podría aplicarse la regla donde se exluyen los pacientes de la Dra.).
- La lista final no incluye el número de teléfono del paciente ya que se asume que se cruzan los datos.

Por mejorar:
- El paciente se debería identificar por RUT. 
- Se le debería agregar el número de teléfono.
- Identificación de grupo etario en el listado original.
- Agregar número de teléfono del paciente.
- Eliminar la función de la fecha y agregar condición en la función de filtrado.

Reformulación del problema:
Se necesita crear un código que lea requerimientos del cliente, dinámicos, sin tener que modificar el código. El objetivo final del ejercicio es obtener un listado de pacientes a los que se les debe informar/recordar de su futura cita, dependiendo de diversas condiciones impuestas por el cliente. 

Mensaje a Customer Success:
"Estimado Equipo!

Se han implementado las nuevas solicitudes del cliente X, las cuales se encuentran funcionando en producción. Ahora no se contactará a ningun paciente de la Dra. Gomez, para el resto de los doctores de cardiología, a sus pacientes se les avisará hasta en 3 ocasiones, en caso de que sea su primera cita médica. Finalmente, para los pacientes del Dr. Martínez se les informará únicamente si son menores de 60 años, edad que se utilizó como referencia a tercera edad. Cualquier reformulación, favor avisar a la brevedad para poder solucionarlo lo antes posible. Quedo atenti.
"
