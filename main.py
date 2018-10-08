def lsys0():                                #Définition du L-système avec ses paramètres
    axiome = 'F'
    prod = {'F':'F[+F][-F]'}
    angleP, angleM = 30, -30
    return axiome, prod, angleP, angleM

def itergen(string, prod):
    '''I/ str, dict
O/ str
       Fait passer une chaîne de caractère issue d'un L-système de l'état N à l'état N+1'''
       
    stringNext = string
       
    for c in string:
        stringNext = ''.join([c if c not in prod.keys() else prod[c] for c in string])      #On prend le caractère de la str, on cherche s'il a une prod associée,
                                                                                                #on applique la prod si elle existe
    return stringNext

def generator(lsys, N):
    '''I/ func, int
O/ str
        Fait boucler N fois la fonction itergen() afin d'avoir la str issue du L-système au rang N
    '''
    lsystem = lsys()        #On prend les paramètres de notre L-système qui nous intéressent
    string = lsystem[0]
    prod = lsystem[1]
    
    for i in range(N):
        string = itergen(string, prod)  #On applique N fois les productions sur la str
    
    return string