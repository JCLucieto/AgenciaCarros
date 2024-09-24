from django.core.management.utils import get_random_secret_key

# Este programa gera chaves randomicas
# Execute na linha de comando (na pasta gerachaves)
# python gerachaves.py

# Exemplo
# ...\gerachaves>python gerachaves.py
# -9j81vn=owjd^1!s=5zf8bm=%-@p$b2o^-v616ke9g2*cjol+!
# ...\gerachaves> 

print (get_random_secret_key())

