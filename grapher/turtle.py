import turtle as trt

def draw(lsysStr, lsys):
    '''I/ str
O/ none
        Dessine le L-système avec la librairie Turtle, itéré N fois en utilisant le générateur (itergen(...), et generator(...))
    '''
    
    nigger = trt.Turtle()   #Génération de la base
    ecwan = trt.Screen()
    brackets = []           #On stockera les positions de "nigger" dès qu'on rencontrera un crochet dans le L-système généré
    
    lsystem = lsys()        #Import du L-système et de ses paramètres
    thetaL = lsystem[2]
    thetaR = lsystem[3]
    
    grammar = {'F': "nigger.forward(50)",                  #Dessin usuels des L-systèmes
               '+': "nigger.left(thetaL)",
               '-': "nigger.right(thetaR)",
               '[': "brackets.append((nigger.pos(), nigger.heading()))",
               ']': "niggerPos, niggerDir = brackets.pop() ; nigger.setheading(niggerDir) ; nigger.setpos(niggerPos)"}
    
    nigger.hideturtle()  #Paramètres généraux
    nigger.left(90)      #On commence de haut en bas
    nigger.speed(10)     #Le tracé est instantané si speed = 0
    
    for char in lsysStr:
        try:
            exec(grammar[char])
        except KeyError:
            pass
