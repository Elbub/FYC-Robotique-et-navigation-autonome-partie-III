# FYC-Robotique-et-navigation-autonome-partie-III

Cas pratique de la partie III de notre cours sur la navigation


# Énoncé

M. Georges, habitant à Beynes, doit prendre un rendez-vous médical. Il peut pour cela se rendre à l'hôpital de Poissy ou à la clinique de Trappes.
Il prend les transports et doit être rentré chez lui avant 20h, donc arriver à la gare de Beynes avant 19h45 au plus tard.
Il veut prendre rendez-vous pour le 07/08/2024. Il a le choix entre 16h30 à Poissy ou 17h30 à Trappes. Le rendez-vous est rapide et il pourra être à la gare une demi-heure plus tard.
Il veut aussi passer le moins de temps possible dans les transports.

## Question 1

Est-il préférable pour lui de prendre rendez-vous à Poissy ou à Trappes ?

## Question 2

Au cas où il y aurait du retard ou si le rendez-vous est plus long que prévu, il souhaite prévoir une heure de marge. Doit-il changer son rendez-vous ?


# Description des données

## platforms_data.json

Ce fichier comporte les informations relatives aux quais. Une gare dispose d'un quai pour chaque ligne qui passe par cette gare. Par exemple, la gare de Poissy dispose d'un quai pour la ligne A et un autre pour la ligne J. Voici la structure d'un quai :
id : {
    ligne
    station
}

## routes.json

Ce fichier comporte les information relatives aux trajets. Un trajet peut être une jonction à pied (passer du quai `Poissy - ligne A` à `Poissy - ligne J`) ou un trajet en train d'un quai au suivant (de `Versailles-Chantiers - ligne N` à `Gare Montparnasse - ligne N`). Voici la structure d'un trajet :
{
    ID du quai de départ
    ID du quai d'arrivée
    heure de départ
    heure d'arrivée
    temps de trajet à pied
}
Les jonctions à pied ont un temps de trajet à pied non null mais pas d'heure de départ ou d'arrivée.
Les trajets en train ont des heure de départ et d'arrivée mais pas de temps de trajet à pied.


# Description des scripts

## main.py

Ce fichier est celui que vous lancerez pour connaître la trajectoire calculée.
La seule modification à faire est de commenter ou décommenter des lignes.

## api.py

Ce fichier comporte la structure des objet représentant un quai (Platform) et un trajet (Route) ainsi que des fonctions permettant d'initialiser leurs variables.
Aucune modification à faire.

## path_planning.py

C'est le coeur du sujet. Il vous faudra remplir toutes les zones marquées de `# ...` et uniquement celles-ci. Le nombre de ligne est indicatif, mais vous pouvez très bien coder l'algorithme en plus ou moins de lignes.

## path_planning_correction.py

Une version corrigée de `path_planning.py`. Ce n'est pas la solution absolue, et il est possible que votre implémentation soit différente mais tout à fait correcte.