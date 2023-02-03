
class juego():
        
    def run(self):
        '''
        0=vacío
        1=cruz
        2=círculo
        '''
        self.tablero=[[0,0,0],[0,0,0],[0,0,0]]
        self.imprimirTablero()
        self.ia=IA()
        self.jugar()
    def jugar(self):
        self.ganadorJ=0
        while True:
            self.jugada()
            self.imprimirTablero()
            if self.ganador(self.tablero):
                break
            print("Jugada enemiga:")
            self.ia.run(self.tablero)
            self.imprimirTablero()
            if self.ganador(self.tablero):
                break
            if not self.comprobarMatriz(self.tablero):
                break
        self.imprimirGanador()

    def comprobarMatriz(self,m):
        for i in m:
            if 0 in i:
                return True
        return False
    
    def imprimirGanador(self):
        if(self.ganadorJ==1):
            print("Ganador: x")
        elif self.ganador==2:
            print("Ganador: o")
        else:
            print("Empate")
    def ganador(self,t):
        for i in range(3):
            if(t[i][0]==t[i][1] and t[i][0]!=0):
                    if(t[i][0]==t[i][2]):
                        self.ganadorJ=t[i][0]
                        return True
            if(t[0][i]==t[1][i] and t[0][i]!=0):
                    if(t[0][i]==t[2][i]):
                        self.ganadorJ=t[0][i]
                        return True
        if(t[0][0]==t[1][1] and t[0][0]!=0):
            if(t[0][0]==t[2][2]):
                self.ganadorJ=t[0][0]
                return True
        if(t[0][2]==t[1][1] and t[0][2]!=0):
            if(t[0][2]==t[2][0]):
                self.ganadorJ=t[0][2]
                return True
        return False

    def imprimirTablero(self):
        for i in self.tablero:
            print('| ',end='')
            for j in i:         
                if(j==0):
                    print(' ',end='')
                elif(j==1):
                    print('x',end='')
                elif(j==2):
                    print('o',end='')
                print(' | ',end='')
            print('\n')

    def jugada(self):
        print("Escriba la casilla en la que desea colocar:")
        j=input()
        self.tablero[int(j[0])][int(j[1])]=1
class IA():
    def run(self,tablero):
        self.profundidadMax=100
        self.tablero=tablero
        self.arbol=[]
        self.valor=1
        self.crearEstados()
        self.Jugada()

    def Jugada(self):
        for i in self.arbol:
            i.comprobarValor()
            if self.valor>i.valor:
                self.valor=i.valor
                self.jugada=i.jugada
                
                
        self.tablero[int(self.jugada[0])][int(self.jugada[1])]=2

    def crearEstados(self):  
        jugador=2 
        for i in range(3):
            for j in range(3):
                if (self.tablero[i][j]==0):
                        t=self.copiarMatriz(self.tablero)
                        t[i][j]=jugador
                        self.jugada=str(i)+str(j)
                        nodo=nodoArbol(0,t,jugador,self.jugada,None)
                        self.arbol.append(nodo)
                        self.continuarArbol(nodo,0)

    def continuarArbol(self,nodo,pr):
        jugador=nodo.jugador%2+1
        gan=juego()
        if(pr<self.profundidadMax and self.comprobarMatriz(nodo.tablero)):
            for i in range(3):
                for j in range(3):
                    if (nodo.tablero[i][j]==0):
                            t=self.copiarMatriz(nodo.tablero)
                            t[i][j]=jugador
                            self.jugada=str(i)+str(j)
                            n=nodoArbol(pr+1,t,jugador,self.jugada,nodo)
                            if not gan.ganador(n.tablero) and self.comprobarMatriz(n.tablero):
                                nodo.hijos.append(n)
                                self.continuarArbol(n,pr+1)
                            else:
                                g=gan.ganador(n.tablero)
                                n.valor=0
                                if( g and gan.ganadorJ==1):
                                    n.valor=1
                                elif(g and gan.ganadorJ==2):
                                    n.valor=-1    
                                nodo.hijos.append(n)     


    def comprobarMatriz(self,m):
        for i in m:
            if 0 in i:
                return True
        return False
    
    def copiarMatriz(self,a):
        b=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(3):
            for j in range(3):
                b[i][j]=a[i][j]
        return b
    

class nodoArbol():
    def __init__(self,id,tablero,jugador,jugada,padre):
        self.id=id
        self.padre=padre
        self.hijos=[]
        self.jugada=jugada
        self.jugador=jugador
        if jugador==1:
            self.valor=2
        else:
            self.valor=-2
        self.tablero=tablero

    def comprobarValor(self):
        if len(self.hijos)!=0:
            for i in self.hijos:
                i.comprobarValor()
                i.asignarPadre()
        else:
            if self.padre!=None:
                self.asignarPadre()
                
    def imprimirTablero(self,t):
        for i in t:
            print('| ',end='')
            for j in i:         
                if(j==0):
                    print(' ',end='')
                elif(j==1):
                    print('x',end='')
                elif(j==2):
                    print('o',end='')
                print(' | ',end='')
            print('\n')
  
    def asignarPadre(self):
        if(self.padre.jugador==1 and self.padre.valor>self.valor):
            self.padre.valor=self.valor
        elif(self.padre.jugador==2 and self.padre.valor<self.valor):
            self.padre.valor=self.valor

try:
    juego().run()
except KeyboardInterrupt:
    print("Se saldrá del juego")