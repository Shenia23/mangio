measurement_units = ['cucharillas','cucharaditas', 'cucharadas','cucharadas soperas','cucharadas de postre','tazas'
                        ,'vasos','cuencos','envases', 'paquetes', 'bolsas','latas', 'botellas','litros', 'paquetes', 
                        'frascos', 'gotas', 'cabezas', 'pellizcos','sobres','dientes','puñados', 'barras', 'cajas','copas',
                        'pizcas','chorros','chorritos','unidades','unidad','racimos','lonchas', 'recetas', 'capas', 'rebanadas', 'gajos', 'tallos', 
                        'cuadrados','ramas', 'ramitas', 'filetes', 'trozos', 'patas', 'muslos', 'cubos', 'tiras', 'bandejas','láminas', 'hojas', 
                        'mitad',"gramos","mililitros"]


for unit in measurement_units:
    if unit[-1:] == 's':
        print(unit)
        singular = unit[:-1]
        measurement_units.append(singular)    

print(measurement_units)

result= ['cucharillas', 'cucharaditas', 'cucharadas', 'cucharadas soperas', 'cucharadas de postre','cucharadas de postre', 'tazas', 'vasos', 'cuencos', 'envases', 'paquetes', 'bolsas', 'latas', 'botellas', 
    'litros', 'paquetes', 'frascos', 'gotas', 'cabezas', 'pellizcos', 'sobres', 'dientes', 'puñados', 'barras', 'cajas', 'copas', 'pizcas', 'chorros', 'chorritos', 'unidades', 'unidad', 'racimos', 
    'lonchas', 'recetas', 'capas', 'rebanadas', 'gajos', 'tallos', 'cuadrados', 'ramas', 'ramitas', 'filetes', 'trozos', 'patas', 'muslos', 'cubos', 'tiras', 'bandejas', 'láminas', 'hojas', 'mitad', 
    'gramos', 'mililitros', 'cucharilla', 'cucharadita', 'cucharada', 'cucharada sopera', 'taza', 'vaso', 'cuenco', 'envase', 'paquete', 'bolsa', 'lata', 'botella', 'litro', 'paquete', 
    'frasco', 'gota', 'cabeza', 'pellizco', 'sobre', 'diente', 'puñado', 'barra', 'caja', 'copa', 'pizca', 'chorro', 'chorrito', 'unidad', 'racimo', 'loncha', 'receta', 
    'capa', 'rebanada', 'gajo', 'tallo', 'cuadrado', 'rama', 'ramita', 'filete', 'trozo', 'pata', 'muslo', 'cubo', 'tira', 'bandeja', 'lámina', 'hoja', 'gramo', 'mililitro']