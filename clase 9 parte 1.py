print("Test del buen estudiante: ")
print("Responda con una 's' si es sí o con una 'n' si es no.")

# Inicialización de variables para el puntaje
puntaje_si = 0
puntaje_no = 0

# Lista de preguntas
preguntas = [
    "¿Deja para después lo que puede hacer ahora?",
    "¿Presta atención en clases?",
    "¿Resuelve sus dudas con el profesor?",
    "¿Prueba sus hipótesis antes de preguntar?",
    "¿Utiliza su tiempo libre para aprender cosas nuevas?",
    "¿Utiliza otra fuente de información para resolver dudas?",
    "¿Estudia solo un día antes de la prueba?",
    "¿A sus amigos solo les gusta pasar el rato?",
    "¿A menudo realiza acciones que no son importantes?",
    "¿Le gustaría no tener que trabajar?",
    "¿Le gusta leer?",
    "¿Le gustan las redes sociales?"
]

# Proceso de hacer preguntas y calcular el puntaje
for i, pregunta in enumerate(preguntas, start=1):
    respuesta = input(pregunta + " ")
    if i in [2, 3, 4, 5, 6, 11] and respuesta.lower() == "n":
        puntaje_no += 1
    elif respuesta.lower() == "s":
        puntaje_si += 1

# Cálculo del total
total = puntaje_no + puntaje_si

# Categorización basada en el puntaje total
print("")
if total < 4:
    print("Usted es un alumno de buen desempeño")
elif total < 7:
    print("Usted es un alumno que puede mejorar")
elif total < 10:
    print("Usted es un alumno con algunos desafíos")
else:
    print("Usted alumno con muchos desafíos")
print("")