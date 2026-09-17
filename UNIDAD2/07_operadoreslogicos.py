edad = 19 
tiene_credencial = True 
tiene_adeudo = True 

es_mayor = edad >= 18 
documento_valido = tiene_credencial 
sin_adeudo = not tiene_adeudo 

autorizado = es_mayor or documento_valido and sin_adeudo
print(autorizado)