#Fichier accueillant les définitions des L-systèmes

def lsys0():                            
    axiome = 'F'
    prod = {'F':'F[+F][-F]'}
    angleP, angleM = 30, 30
    return axiome, prod, angleP, angleM

def plant4():
    axiom='X'
    rules={'X':'F[+X][-X]FX','F':'FF'}
    angleL, angleR = 25.7, 25.7    
    return axiom, rules, angleL, angleR

def pythagore():
    axiom='0'
    rules={'0':'1[+0]-0','1':'11'}
    angleL, angleR = 45., 45.
    return axiom,rules, angleL, angleR    

def Sierpinski1():
    axiom='A'
    rules={'A':'+B-A-B+','B':'-A+B+A-'}
    angleL, angleR = 60., 60.
    return axiom,rules, angleL, angleR    
    
def Sierpinski2():
    axiom='F-G-G'
    rules={'F':'F-G+F+G-F','G':'GG'}
    angleL, angleR = 120., 120.
    return axiom,rules, angleL, angleR    

def dragon():
    axiom='FX'
    rules={'F':'F','X':'X+YF+','Y':'-FX-Y'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    

def island():
    axiom='F+F+F+F'
    #rules={'F':('F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF',0.,1.),'f':('ffffff',0.,1.),'+':('+',90.,0.),'-':('-',-90.,0.)}
    rules={'F':'F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF','f':'ffffff'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    
    
def Koch():
    axiom='F-F-F-F'
    rules={'F':'F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    
    
def Koch_square():
    axiom='F-F-F-F'
    rules={'F':'FF-F-F-F-FF'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    
    
def Koch_rect():
    axiom='F-F-F-F'
    rules={'F':'FF-F+F-F-FF'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    
    
def Koch_sing():
    axiom='F-F-F-F'
    rules={'F':'FF-F--F-F'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    

def FASS():
    axiom='F'
    rules={'F':'F+G++G-F--FF-G+','G':'-F+GG++G+F--F-G'}
    angleL, angleR = 60., 60.
    return axiom,rules, angleL, angleR    

def FASS2():
    axiom='-G'
    rules={'F':'FF-G-G+F+F-G-GF+G+FFG-F+G+FF+G-FG-G-F+F+GG-',
           'G':'+FF-G-G+F+FG+F-GG-F-G+FGG-F-GF+F+G-G-F+F+GG'}
    angleL, angleR = 90., 90.
    return axiom,rules, angleL, angleR    

def plant0():
    axiom='F'
    rules={'F':'F[+F]F[-F]F'}
    angleL, angleR = 20., 20. 
    return axiom, rules, angleL, angleR
    
def plant1():
    axiom='F'
    rules={'F':'F[+F]F[-F][F]'}
    angleL, angleR = 25.7, 25.7
    return axiom, rules, angleL, angleR
    
def plant2():
    axiom='F'
    rules={'F':'FF-[-F+F+F]+[+F-F-F]'}
    angleL, angleR = 22.5, 22.5
    return axiom, rules, angleL, angleR
    
def plant3():
    axiom='X'
    rules={'X':'F[+X]F[-X]+X','F':'FF'}
    angleL, angleR = 20.0, 20.0
    return axiom, rules, angleL, angleR
    
def plant5():
    axiom='X'
    rules={'X':'F-[[X]+X]+F[+FX]-X','F':'FF'}
    angleL, angleR = 22.5, 22.5
    return axiom, rules, angleL, angleR

def flocon_de_Koch():
    axiom='F--F--F'
    rules={'F':'F+F--F+F'}
    angleL, angleR = 60., 60.
    return axiom,rules, angleL, angleR