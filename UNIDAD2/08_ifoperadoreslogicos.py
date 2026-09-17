edad = 18
tiene_credencial = True 
tiene_adeudo = False

if edad >= 18:
    es_mayor=True
else:
    es_mayor=False

documento_valido = tiene_credencial
sin_adeudo = not tiene_adeudo
if es_mayor and documento_valido and sin_adeudo:
    autorizado = True
else:
    autorizado = False
autorizado = es_mayor and documento_valido and sin_adeudo
print(autorizado)