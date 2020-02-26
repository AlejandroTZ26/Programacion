# El format se utiliza para dar una vista mas profesional 

def main():
  intBase = 7
  intAltura = 5
  fltAreaTriangulo=(intBase*intAltura)/2
  txt = "Area: {2:0.2f} ( {0} por {1} entre dos )"
  print(txt.format(intBase, intAltura, fltAreaTriangulo))

# El orden de los parámetros proporcionados a format es de base cero.
# {2:0,0f} es un flotante sin decimales.