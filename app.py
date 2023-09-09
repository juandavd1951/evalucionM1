notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

resutado ={}

for  nombres, notas in notas_estudiantes.items():  
    resutado = {nombre:sum (notas)for nombre,notas in notas_estudiantes.items()}  
    
print (resutado)
    






