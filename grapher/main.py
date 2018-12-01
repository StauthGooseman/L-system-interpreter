import turtle as trt

D = 5
p = 0.5

def itergen(string, prod):
    '''I/ str, dict
O/ str
       Fait passer une chaîne de caractère issue d'un L-système de l'état N à l'état N+1'''
       
    stringNext = string
       
    for c in string:
        stringNext = ''.join([c if c not in prod.keys() else prod[c] for c in string])          #On prend le caractère de la str, on cherche s'il a une prod associée,
                                                                                                #On applique la prod si elle existe
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
    nigger = trt.Turtle()   #Génération de la base
    ecwan = trt.Screen()
    ecwan.title('L-system drawer')
    ecwan.setup(1., 1.)
    brackets = []           #On stockera les positions de "nigger" dès qu'on rencontrera un crochet dans le L-système généré
    
    lsystem = lsys()        #Import du L-système et de ses paramètres
    thetaL = lsystem[2]
    thetaR = lsystem[3]
    
    grammar = {'F': "nigger.forward(D)",                  #Dessin usuels des L-systèmes
               '+': "nigger.left(thetaL)",
               '-': "nigger.right(thetaR)",
               '[': "D *= p ; brackets.append((nigger.pos(), nigger.heading()))",
               ']': "D /= p ; niggerPos, niggerDir = brackets.pop() ; nigger.setheading(niggerDir) ; nigger.setpos(niggerPos)"}
    
    nigger.hideturtle()  #Paramètres généraux
    nigger.left(90)      #On commence de haut en bas
    nigger.speed(10)     #Le tracé est instantané si speed = 0
    trt.tracer(False)
    
    nigger.pu()
    # nigger.setpos(0,-385)
    nigger.pd()
    
    for char in drawnStr:
        try:
            exec(grammar[char])
        except KeyError:
            pass
    
    ecwan.exitonclick()

def launcher(lsys = lsys0, N = 3):
    trt.TurtleScreen._RUNNING = True
    lsysSTR = generator(lsys, N)
    draw(lsysSTR, lsys)

launcher(dragon, 15)