#fonction qui prend en entre une liste de liste ainsi que la capacite du sac
def knapSack(totalWeight, objects):
    #la capacite du sac qui a jour a chaque boucle
    currentWeight = 0
    #liste qui stocke les objets jusqu'a saturation du sac a dos
    subSet = []
    #boucle qui verifie si le poids max est superieur ou egal a un objet plus la capacite du sac au moment donnee
    #si la condition est rempli alors 
    for counter in range(len(objects)):
        if currentWeight + objects[counter][-1] <= totalWeight:
            currentWeight += objects[counter][-1]
            subSet.append(objects[counter])
    #renvoie la liste pleine contenant des objets une fois le sac remplie
    return subSet

#fonction appele au lancement du programme
def retrivevingData():
    #on creer une liste de liste qui repertorie chaque objet avec sa valeur et son poid
    objects = [['L', 12, 10],['E', 10, 7],['C', 8, 5],['F', 7, 4],['H', 7, 4],['K', 6, 4],['D', 5, 2],['N', 4, 1],['A', 4, 2],['J', 3, 1],['I', 3, 2],['B', 3, 2],['M', 2, 2],['G', 1, 1]]
    #la capacite maximum du sac a dos
    totalWeight = 26
    #on appel la fonction pour selectionner les objets les plus pertinent
    return knapSack(totalWeight, objects)

print("D'apres la methode Gloutonne, voici les objets a privilegier :")
print(retrivevingData())