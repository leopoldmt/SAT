import numpy as np

class DPLL(object):
    
    def __init__(self, C, nbVar) -> None : 
        self.clauses = C
        self.nbVar = nbVar
        
        self.S = np.empty((0, 3), int)
        self.clauses_unitaires = np.full(len(C), False)
        self.litteral_pur = np.full(self.nbVar, 0)
        self.importance_variable = np.full((self.nbVar,2), 0, dtype = float)
        self.clauses_satisfaites = np.full(len(C), False)
                
    
    def test_consistance(self):
        
        self.clauses_unitaires = np.full(len(self.clauses), False)
        self.litteral_pur = np.full(self.nbVar, None)
        self.importance_variable = np.full((self.nbVar,2), 0, dtype = float)
        self.clauses_satisfaites = np.full(len(self.clauses), False)

        list_affectations = self.S[:,0] * self.S[:,1]
        #print("liste affectations = ", list_affectations)
        
        i = 0
        for clause in self.clauses:
            nf = 0
            for litteral in clause:
                if litteral in list_affectations:
                    self.litteral_pur[(abs(litteral) - 1)] = 0
                    self.clauses_satisfaites[i] = True
                    nf += 2
                    break
                elif -litteral in list_affectations:
                    self.litteral_pur[(abs(litteral) - 1)] = 0
                    nf += 0
                else:
                    nf += 1
                    
                    if np.sign(litteral) == -1:
                        self.importance_variable[(abs(litteral) - 1), 0 ] += 1/len(clause)
                    else :
                        self.importance_variable[(abs(litteral) - 1), 1 ] += 1/len(clause)
                    
                    if self.litteral_pur[(abs(litteral) - 1)] == None:
                        self.litteral_pur[(abs(litteral) - 1)] = np.sign(litteral)                        
                    elif self.litteral_pur[(abs(litteral) - 1)] != np.sign(litteral):
                        self.litteral_pur[(abs(litteral) - 1)] = 0
            
            if nf == 0:
                return False
            elif nf == 1:
                self.clauses_unitaires[i] = True
           
            i += 1
        return True
    
    def choose_first_variable(self):
            
        for clause in self.clauses:
            for litteral in clause:
                if len(self.S) == 0:
                    self.S = np.append(self.S, np.array([[abs(litteral),np.sign(litteral),-np.sign(litteral)]]), axis = 0)
                    return "finish"
                else:
                    if abs(litteral) not in self.S[:,0]:
                        self.S = np.append(self.S, np.array([[abs(litteral),np.sign(litteral),-np.sign(litteral)]]), axis = 0)
                        return "finish"
                    
    def intellience_choice(self):
        idx = np.unravel_index(self.importance_variable.argmax(), self.importance_variable.shape)
        
        if idx[1] == 0:
            self.S = np.append(self.S, np.array([[(idx[0]+1),-1,1]]), axis = 0)
        else:
            self.S = np.append(self.S, np.array([[(idx[0]+1),1,-1]]), axis = 0)
                    
    def choose_litteral_pur(self,litteraux_purs):
        self.S = np.append(self.S, np.array([[ (litteraux_purs[0] + 1) , self.litteral_pur[litteraux_purs[0]], -self.litteral_pur[litteraux_purs[0]]]]), axis = 0)
    
    def choose_new_variable(self):
        
        #print("S = ", self.S)
        
        idx_clause_unitaire = np.where(self.clauses_unitaires == True)[0]
        #print(self.clauses_unitaires)
        #print("idx = ", idx_clause_unitaire)
        
        litteraux_purs = np.where(self.litteral_pur == 1)[0]
        #print(self.importance_variable)
        
        if len(idx_clause_unitaire) == 0:
            #print("No clause unitaire")
            if len(litteraux_purs) != 0 : #litteral pur
                self.choose_litteral_pur(litteraux_purs)
            else:
                self.intellience_choice()
        else:
            clause = self.clauses[idx_clause_unitaire[0]]
             #print("clause unitaire", clause)
        
            for litteral in clause:            
                if abs(litteral) not in self.S[:,0]:
                        self.S = np.append(self.S, np.array([[abs(litteral),np.sign(litteral),-np.sign(litteral)]]), axis = 0)
                        return "finish"
        
    
    def depilate(self):
        lastS = self.S[(len(self.S)-1)]
        vp = lastS[2]
        X = lastS[0]
        self.S = self.S[0:(len(self.S)-1)]
        return vp, X
    
    def backtrack(self):
        #n = self.nbVar
        finish = False
        
        i = 0
        echecs = 0
        while finish == False:
            #print("i = ",i, self.S)
            #print("clauses = ", self.clauses)
            if self.test_consistance():
                #print("consistant",self.S)
                #print("clauses satisfaites = ", self.clauses_satisfaites)
                if np.sum(self.clauses_satisfaites) == len(self.clauses):
                    finish = True
                else:
                    self.choose_new_variable()
            else:
                echecs += 1
                #print("non consistant",S,C)
                vp,X = self.depilate()
                while (len(self.S) > 0) and (vp == None):
                    vp,X = self.depilate()
                if vp!=None :
                    self.S = np.append(self.S, np.array([[X,vp,None]]), axis = 0)
                else:
                    finish = True
            i += 1
                    
        return self.S, i, echecs
    
                
    def verif_S(self):
        verif =  []
        for i in self.S:
            verif.append(i[0]*i[1])
            
        idx = np.argsort(np.abs(np.array(verif)))
    
        return np.array(verif)[idx]