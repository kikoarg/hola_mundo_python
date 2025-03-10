# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(f'el valor de texto_1 ({texto_1}) es mayor alfabeticamente al valor de texto_2 ({texto_2})')
else:
    print(f'el valor de texto_2 ({texto_2}) es mayor alfabeticamente al valor de texto_1 ({texto_1})')
# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
int_numero_1 = int(texto_1)
int_numero_2 = int(texto_2)
print(f'--------------')
if int_numero_1 > int_numero_2:
    print(f' {int_numero_1} es mayor que {int_numero_2}')
elif int_numero_2 > int_numero_1:
    print(f' {int_numero_2} es mayor que {int_numero_1}')
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
