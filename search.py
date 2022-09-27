# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from cmath import exp
from email import utils
from inspect import CORO_SUSPENDED
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    #Markel
    #Creamos una clase Nodo que contenga los siguientes datos
    #   coordenada: la coordenada del propio nodo
    #   camino: el camino que debe realizar el pacman para llegar a él
    class Nodo:
        def __init__(self , coordenada, camino=[]):
            self.coordenada = coordenada
            self.camino = camino
        
        def print():
            #Metodo de prueba para ir comprobando si funciona
            #Este metodo se asemeja a toString() en Java
            print("coordenada: "+str(self.coordenada))
            print()
            print("camino: "+str(self.camino))
    
    #Obtenemos la coordenada inicial
    coordenadaInicial = problem.getStartState()
    #Creamos un Nodo con dicha coordenada con la clase que habiamos creado
    nodoInicial = Nodo(coordenada= coordenadaInicial)
    #Creamos una pila para ir almacenando los Nodos por visitar
    sinExplorar = util.Stack()
    #Introducimos el nodoInicial a la pila
    sinExplorar.push(nodoInicial)
    #Creamos una lista tipo set para ir almacenando las coordenadas visitadas
    explorados = set() #En un set es imposible que se repitan elementos


    while not sinExplorar.isEmpty(): 
        #Mientras no se termine la pila
        nodoActual = sinExplorar.pop()
        #Vamos sacando nodos de uno en uno 
        if nodoActual.coordenada not in explorados:
            #Y comprobamos si el nodo que hemos sacado ya lo hemos visitado
            explorados.add(nodoActual.coordenada)
            #Si no es asi, lo introducimos a el set marcandolo como visitado
            if problem.isGoalState(nodoActual.coordenada):
                #En caso de que el nodo que estemos analizando sea el final del camino hacemos return
                return nodoActual.camino
            vecinos = problem.getSuccessors( nodoActual.coordenada )
            #En caso contrario vamos sacando sus nodos vecinos
            for vecino in vecinos:
                #Por cada nodo vecino que tenga
                #Vamos a completar el camino hacia ese nodo uniendo el camino que traia el anterior
                #con la direccion que trae este
                caminoNuevo = nodoActual.camino + [vecino[1]]
                #y con este camino y la coordenada, crearemos un nuevoNodo 
                nodoNuevo = Nodo(coordenada = vecino[0], camino = caminoNuevo)
                #Finalmente este nuevo nodo lo meteremos en la pila para posteriormente analizarlo
                sinExplorar.push(nodoNuevo)
    
    #finalmente devolvemos el camino que tiene el ultimo nodo analizado
    return nodoActual.camino    
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
   
    fringe = util.Queue() #frontera (sin explorar), candidatos
    closed = set() #explorados
    lista_direcciones = [] #movimientos para el pacman
    
    #primer estado, le meto las coordenadas iniciales y 
    #la lista de direcciones por las que alcanzar esa 
    #posicion. Al principio está vacía ya que es el nodo
    #inicial

    fringe.push((problem.getStartState(), lista_direcciones))
    
    #mientras tengamos frontera:
    while not fringe.isEmpty():
        
        
        actual_estado, actual_camino = fringe.pop() #sacamos la coordenada y
                                                    #el camino para llegar a ella
        
        if problem.isGoalState(actual_estado): #si hemos llegado al punto blanco...
            return actual_camino
        
        #si no tenemos explorada la coordenada actual (esto evita explorar dos veces la misma posición)
        elif actual_estado not in closed:
            closed.add(actual_estado) #añadimos a explorados la coordenada
            sucesores = problem.getSuccessors(actual_estado) #sacamos los de alrededor
            for coord, movimiento, coste in sucesores: #de todos los de alrededor...
                #if coord not in closed: #si cada coordenada no está explorada
                nuevalistadirecciones = actual_camino + [movimiento] #la añadimos a la lista de 
                                                                    #movimientos que vamos actualizando sin parar
                fringe.push((coord, nuevalistadirecciones)) #metemos en la cola la coordenada 
                                                            # y el camino para llegar a ella
            
    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
