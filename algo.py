# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie a rendre
import math


montant = 324.37
resultat = {}
id_resultat = 0

# valeur des pieces disponibles en euro trié dans l'ordre croissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]
nom_pieces = ['2€', '1€', '50 cents', '20 cents', '10 cents', '5 cents', '2 cents', '1 cent']
## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie(somme, ListeMontant) :

    # tableau de nombre de piece max a rendre selon le tableau de pieces
    ListeNbPiece=[0 for y in ListeMontant]

    # parcours de la liste des pieces
    for k in range(len(ListeMontant)) :

        # recupere le nombre de piece selon le quotient (entier //)
        ListeNbPiece[k]=somme//ListeMontant[k]

        # somme restante a deduire du montant
        somme=round(somme%ListeMontant[k], 2)

    return somme, ListeNbPiece

Somme_resultat = Monnaie(montant, pieces)[0]
Monnaie_resultat = Monnaie(montant, pieces)[1]

for i in nom_pieces:
    resultat[i]=Monnaie_resultat[id_resultat]
    id_resultat += 1

print('Somme =',math.floor(Somme_resultat))
print('-------------')

for i in resultat:
    print(i, '=', math.floor(resultat.get(i)))
print('-------------')