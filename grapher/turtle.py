import turtle as trt

D = 100
p = 0.5

def draw(lsysStr, lsys):
    '''I/ str
O/ none
        Dessine le L-système avec la librairie Turtle, itéré N fois en utilisant le générateur (itergen(...), et generator(...))
    '''
    
    drawnStr = lsysStr[:]
    nigger = trt.Turtle()   #Génération de la base
    ecwan = trt.Screen()
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
    # trt.tracer(False)
    
    nigger.pu()
    nigger.setpos(0,-385)
    nigger.pd()
    
    for char in drawnStr:
        try:
            exec(grammar[char])
        except KeyError:
            pass
    
    ecwan.exitonclick()