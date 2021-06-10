Code by : MAYTIE Léopold

-Intro:

Ce programme est une implémentation itérative de l'algorithme DPLL.


-Debut:

Placez vous dans le répertoire où se trouve le fichier run_DPLL.py : 
	cd .../TP

Lancer le programme à l'aide de la commande python3 :
	python3 run_DPLL.py

Il est directement possible de fournir un fichier d'extension .cnf lors de l'exécution :
	python3 run_DPLL.py .../uf20-01.cnf


-Commandes:

Si vous ne rentrez aucun fichier vous pourrez toujours en donner un au programme par la suite après l'affichage de : "Veuillez rentrer une commande : "
	Veuillez rentrer une commande : 
	.../uf20-01.cnf

Vous pouvez aussi spécifier au programme le chemin pour accéder à vos fichiers plutôt que de l'écrire entièrement à chaque fois. 
	Veuillez rentrer une commande : 
	set direcory mon/chemin/vers/mes/donnees


Après l'affichage des résultats le programme vous demendera si c'est possible (problème satisfiable) si vous voulez affichez toutes les solutions possibles du problème : "souhaitez vous voir toutes les solutions possibles [O/N] ?"
Vous pourrez alors rentrer "Oui" ou "O" si vous voulez les afficher ou "Non" ou "N" sinon
	souhaitez vous voir toutes les solutions possibles [O/N] ?
	O
OU
	souhaitez vous voir toutes les solutions possibles [O/N] ?
	N

Le programme vous demandera ensuite de rentrer une autre commande "Veuillez rentrer une commande : "
Vous pouvez alors soit donner un autre fichier .cnf si vous voulez ou écrire "quit" si vous voulez sortir du programme
	Veuillez rentrer une commande : 
	quit
OU
	Veuillez rentrer une commande : 
	uf50-01.cnf

Résumé		monfichier.cnf	-> exécuter le programme sur monfichier
		set directory	-> donner le chemin où se trouve les données au programme
		quit			-> quitte le programme
		O 				-> afficher toutes les solutions
		N 				-> sauter l'affichage de toutes les solutions


-Résultats:

Les résultats sont présentés sous cette forme :

....................................................

temps pour trouver la première solution :  temps en secondes
Solution possible :  Première solution que l'algorithme a trouvé

....................................................

temps pour trouver toutes les solutions :  temps en secondes
nombre modèles :  nombre de modèles possibles


-Précisions:

Pour une question de rapidité l'algorithme pour trouver la première réponse s'arrête lorsque toutes les clauses sont satisfaites et non lorsque toutes les variables sont affectées. Il est donc normal que certaines variables ne soient pas présentent dans la première solution que l'algorithme a trouvé. Cela signifie que cette variable peut être affectée à True ou False, cela ne changera rien.
