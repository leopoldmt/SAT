from DPLL import DPLL
from DPLLV2 import DPLLComplet
import time
import sys
import numpy as np

class Systeme(object):
    
    def __init__(self) :
        
        self.filename = None
        
    def read_file(self):
    
        file = open(self.filename , "r")
        lignes = file.readlines()
        
        list_clauses = []
        for ligne in lignes:
            clause = []
            first_line = False
            pos = 0
            for ch in ligne.split():
                pos = pos + 1
                
                if ch=='c' or ch=='0' or ch=='%':
                    break
                elif ch=='p':
                    first_line = True
                    
                if first_line == True:
                    if pos == 3:
                        nbVar = int(ch)
                    if pos == 4:
                        nbClauses = int(ch)
                if first_line == False : 
                    clause.append(int(ch))
                    
            if clause:
                list_clauses.append(clause)
                
        return list_clauses, nbClauses, nbVar

    
    def run(self):

        nbTours = 0
        directory = ""
        
        while True:
            if (len(sys.argv) > 1) and (nbTours==0) : 
                self.filename = directory + sys.argv[1]
                clauses, nbClauses, nbVar = self.read_file()
            else:
                while True:
                    print("Veuillez rentrer une commande : ")
                    try:
                        commande= input()
                        self.filename = directory + commande
                        res = commande.split() 
                        clauses, nbClauses, nbVar = self.read_file()
                        break
                    except:
                        if commande.upper() == "QUIT":
                            sys.exit()
                        elif (len(res) > 0) and (res[0].upper() == "SET") and (res[1].upper() == "DIRECTORY"):
                            try:
                                directory = res[2]
                            except:
                                directory = ""
                        else:
                            print("fichier invalide")
            
            algo = DPLL(clauses, nbVar)
            
            start1 = time.time()
            S, i, echecs = algo.backtrack()
            end1 = time.time() - start1
            
            print("\n....................................................\n")
            print("temps pour trouver la première solution : ", end1)   
            print("Solution possible : ", algo.verif_S())
        
            if len(S)!=0:
                
                algo2 = DPLLComplet(clauses, nbVar)

                start2 = time.time()
                Solutions = algo2.backtrack()
                end2 = time.time() - start2
                
                print("\n....................................................\n")
                print("temps pour trouver toutes les solutions : ", end2)   
                print("nombre modèles : ", len(Solutions))
                
                print("\nsouhaitez vous voir toutes les solutions possibles [O/N] ?")
                while True:
                    reponse = input().upper()
                    if reponse == "O" or reponse == "OUI":
                        print("tous les modèles possibles : \n")
                        for i in range(len(Solutions)):
                            verif =  []
                            for i in Solutions[i]:
                                verif.append(i[0]*i[1])
                                
                            idx = np.argsort(np.abs(np.array(verif)))
                            verif = np.array(verif)[idx]
                            print(verif,"\n")
                        break
                    elif reponse == "N" or reponse == "NON":
                        break
                    else:
                        print("Désolé je n'ai pas compis votre réponse ")
                
            else:
                print("\n....................................................\n")
                print("temps pour trouver que l'instance est insatisfiable : ", end1)   
                print("instance insatisfiable")
            
            nbTours += 1