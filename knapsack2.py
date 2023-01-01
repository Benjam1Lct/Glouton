# On suppose qu'on a une liste d'objets trie par valeur dans l'ordre decroissant, chaque objet ayant une valeur et son poids
objects = [['L', 12, 10],['E', 10, 7],['C', 8, 5],['F', 7, 4],['H', 7, 4],['K', 6, 4],['D', 5, 2],['N', 4, 1],['A', 4, 2],['J', 3, 1],['I', 3, 2],['B', 3, 2],['M', 2, 2],['G', 1, 1]]

# On a également un poids maximal que le sac à dos peut supporter
max_weight = 26
save_weight = max_weight

# On initialise la valeur totale à 0 et la liste des objets pris à vide
total_value = 0
total_weigtht = 0
taken_objects = []

# On parcourt la liste d'objets
for object in objects:
  # Si l'objet tout entier peut être ajouté au sac à dos
  if object[2] <= max_weight:
    # On ajoute la valeur de l'objet à la valeur totale
    total_value += object[1]
    # On ajoute le poids de l'objet au poids total
    total_weigtht += object[2]
    # On enlève le poids de l'objet au poids maximal restant
    max_weight -= object[2]
    # On ajoute l'objet à la liste des objets pris
    taken_objects.append(object)
  else:
    # Si l'objet ne peut pas être ajouté tout entier, on ajoute seulement la partie qui peut être prise
    total_value += object[1] / object[2] * max_weight
    # on calculer si la quantite prise est null, si oui on enregistre pas
    if object[1] / object[2] * max_weight == 0.0:
        pass
    # sinon on ajoute l'objet à la liste des objets pris en indiquant la quantité prise
    else:
        taken_objects.append([object[0], object[1] / object[2] * max_weight,max_weight])
        # On ajoute le poids de l'objet au poids total
        total_weigtht += max_weight
    # On met le poids maximal restant à 0 car le sac à dos est plein
    max_weight = 0

# On affiche la valeur totale des objets pris et la liste des objets pris
print('Valeur total =',total_value)
print('Poids du sac a la fin =',total_weigtht,'/',save_weight)
print('Objets stockés dans le sac :',taken_objects)
