import turtle as trt

D = 100
p = 0.8
x0, y0 = 0, -385

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

def draw(lsysStr, lsys):
    '''I/ str
O/ none
        Dessine le L-système avec la librairie Turtle, itéré N fois en utilisant le générateur (itergen(...), et generator(...))
    '''
    
    drawnStr = lsysStr[:]
    
    abitbol = trt.Turtle()   #Génération de la base
    
    roiDeLaClasse = trt.Screen()            #Paramètres de la fenêtre
    roiDeLaClasse.title('L-system drawer')
    roiDeLaClasse.setup(1., 1.)
    
    brackets = []           #On stockera les positions de "abitbol" dès qu'on rencontrera un crochet dans le L-système généré
    
    lsystem = lsys()        #Import du L-système et de ses paramètres
    thetaL = lsystem[2]
    thetaR = lsystem[3]
    
    grammar = {'F': "abitbol.forward(D)",                  #Dessin usuels des L-systèmes
               '+': "abitbol.left(thetaL)",
               '-': "abitbol.right(thetaR)",
               '[': "D *= p ; brackets.append((abitbol.pos(), abitbol.heading()))",
               ']': "D /= p ; abitbolPos, abitbolDir = brackets.pop() ; abitbol.setheading(abitbolDir) ; abitbol.setpos(abitbolPos)"}
    
    abitbol.hideturtle()  #Paramètres généraux
    abitbol.left(90)      #On commence de haut en bas
    abitbol.speed(10)     #Le tracé est instantané si speed = 0
    trt.tracer(False)
    
    abitbol.pu()
    abitbol.setpos(x0, y0)
    abitbol.pd()
    
    for char in drawnStr:
        try:
            exec(grammar[char])
        except KeyError:
            pass
    
    roiDeLaClasse.update()
    roiDeLaClasse.exitonclick()

def launcher(lsys = lsys0, N = 3):
    trt.TurtleScreen._RUNNING = True
    lsysSTR = generator(lsys, N)
    draw(lsysSTR, lsys)

launcher(lsys0, 7)