#Fichier accueillant les définitions des L-systèmes

def lsys0():                            
    axiom = 'F'
    prod = {'F':'F[+F][-F]'}
<<<<<<< HEAD
    angleP, angleM = 30, 30
    longueur, facteur = 100, 0.5
    return axiom, prod, angleP, angleM, longueur, facteur
=======
    angleP, angleM = 30, -30
    return axiome, prod, angleP, angleM
>>>>>>> parent of 309a6cc... updated turtle

def plant4():
    axiom='X'
    rules={'X':'F[+X][-X]FX','F':'FF'}
<<<<<<< HEAD
    angleL, angleR = 25, 25   
    longueur, facteur = 40, 0.2
    return axiom, rules, angleL, angleR, longueur, facteur

def dragon():
    axiom='FX'
    rules={'F':'F','X':'X+YF+','Y':'-FX-Y'}
    angleL, angleR = 90., 90.
    longueur, facteur = 40, 0.8
    return axiom,rules, angleL, angleR, longueur, facteur
=======
    angleL, angleR = 25.7, -25.7    
    return axiom, rules, angleL, angleR
>>>>>>> parent of 309a6cc... updated turtle

def pythagore():
    axiom='0'
    rules={'0':'1[+0]-0','1':'11'}
    angleL, angleR = 45., -45.
    return axiom,rules, angleL, angleR    

def Sierpinski1():
    axiom='A'
    rules={'A':'+B-A-B+','B':'-A+B+A-'}
    angleL, angleR = 60., -60.
    return axiom,rules, angleL, angleR    
    
def Sierpinski2():
    axiom='F-G-G'
    rules={'F':'F-G+F+G-F','G':'GG'}
<<<<<<< HEAD
    angleL, angleR = 120., 120.
    return axiom,rules, angleL, angleR
=======
    angleL, angleR = 120., -120.
    return axiom,rules, angleL, angleR    

def dragon():
    axiom='FX'
    rules={'F':'F','X':'X+YF+','Y':'-FX-Y'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    
>>>>>>> parent of 309a6cc... updated turtle

def island():
    axiom='F+F+F+F'
    #rules={'F':('F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',0.,1.),'f':('ffffff',0.,1.),'+':('+',90.,0.),'-':('-',-90.,0.)}
    rules={'F':'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF','f':'ffffff'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    
    
def Koch():
    axiom='F-F-F-F'
    rules={'F':'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    
    
def Koch_square():
    axiom='F-F-F-F'
    rules={'F':'FF-F-F-F-FF'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    
    
def Koch_rect():
    axiom='F-F-F-F'
    rules={'F':'FF-F+F-F-FF'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    
    
def Koch_sing():
    axiom='F-F-F-F'
    rules={'F':'FF-F--F-F'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    

def FASS():
    axiom='F'
    rules={'F':'F+G++G-F--FF-G+','G':'-F+GG++G+F--F-G'}
    angleL, angleR = 60., -60.
    return axiom,rules, angleL, angleR    

def FASS2():
    axiom='-G'
    rules={'F':'FF-G-G+F+F-G-GF+G+FFG-F+G+FF+G-FG-G-F+F+GG-',
           'G':'+FF-G-G+F+FG+F-GG-F-G+FGG-F-GF+F+G-G-F+F+GG'}
    angleL, angleR = 90., -90.
    return axiom,rules, angleL, angleR    

def plant0():
    axiom='F'
    rules={'F':'F[+F]F[-F]F'}
    angleL, angleR = 20., -20. 
    return axiom, rules, angleL, angleR
    
def plant1():
    axiom='F'
    rules={'F':'F[+F]F[-F][F]'}
    angleL, angleR = 25.7, -25.7
    return axiom, rules, angleL, angleR
    
def plant2():
    axiom='F'
    rules={'F':'FF-[-F+F+F]+[+F-F-F]'}
    angleL, angleR = 22.5, -22.5
    return axiom, rules, angleL, angleR
    
def plant3():
    axiom='X'
    rules={'X':'F[+X]F[-X]+X','F':'FF'}
    angleL, angleR = 20.0, -20.0
    return axiom, rules, angleL, angleR
    
def plant5():
    axiom='X'
    rules={'X':'F-[[X]+X]+F[+FX]-X','F':'FF'}
    angleL, angleR = 22.5, -22.5
    return axiom, rules, angleL, angleR

def flocon_de_Koch():
    axiom='F--F--F'
    rules={'F':'F+F--F+F'}
    angleL, angleR = 60., -60.
    return axiom,rules, angleL, angleR