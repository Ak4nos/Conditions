nombre_a_gauche = input("Entrez un nombre : ")
nombre_a_droite = input("Entrez un nombre : ")
operation = input("Operation? (+, -, *, /) : ")
resultat = 0
if nombre_a_gauche.isnumeric()== False and nombre_a_droite.isnumeric()==False:
    print("Erreur: les deux nombres doivent être des nombres entiers")
else :
  nombre_a_gauche = int(nombre_a_gauche)
  nombre_a_droite = int(nombre_a_droite)
  if operation == "+":
    resultat = nombre_a_gauche + nombre_a_droite
  elif operation == "-":
    resultat = nombre_a_gauche - nombre_a_droite
  elif operation == "*":
    resultat = nombre_a_gauche * nombre_a_droite
  elif operation == "/":
    if nombre_a_droite == 0:
      print("Erreur: impossible de diviser par zéro.")
    else:
      resultat = nombre_a_gauche / nombre_a_droite
  else:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
  print(f"Le résultat de l'opération est: {resultat}")