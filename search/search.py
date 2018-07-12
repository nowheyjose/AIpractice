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
'''
def dfsUtil(problem, v, visited):
    visited[v] = True
    print v,

    for i in problem:
        if visited[v] = False:
            self.dfsUtil(problem.getSuccessor,v, visited)
'''
#this general helper function referenced from kevinkoo001
#helped me figure out how to keep track of the paths traversed
#using a dictionary
#the solution reduces memory usage by creating a single parent array
def getPath(goal, prevNodes, nxtMoves):
    answer = []
    currVertex = goal

    #traverse through previous vertices
    while currVertex in prevNodes:
        #add set of directions to answer while traversing nodes
        answer.append(nxtMoves[currVertex])
        #set next coordinate to find the direction taken to
        #reach it
        currVertex = prevNodes[currVertex]

    #the path is appended in reverse since the start was
    #the final node/goal
    #we need to flip the path so it reads the correct answer
    answer.reverse()

    return answer



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    """
    ***** Testing output results:  *****
    Start: (5, 5)
    Is the start a goal? False
    Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
    """
    start = problem.getStartState()
    #track visited nodes in maze
    visited = []
    #stop if already at goal, there's nothing to return
    if problem.isGoalState(start):
        return visited

    #util.Stack push(self,item), pushes the 'item' to fringe/exploring
    exploring = util.Stack()
    exploring.push(start)

    #create dictionaries that can store pacman's movement
    parentPath = {}
    pastMoves = {}

    while not exploring.isEmpty():
        #need to know the current state and next move of agent
        curr = exploring.pop()
        #add visited nodes in maze to visited
        visited.append(curr)
        for (nxtMove, direction, cost) in problem.getSuccessors(curr):
            if nxtMove not in visited:
                visited.append(nxtMove)
                #record path and direction taken
                parentPath[nxtMove] = curr
                pastMoves[nxtMove] = direction
                if problem.isGoalState(nxtMove):
                    return getPath(nxtMove, parentPath, pastMoves)
                exploring.push(nxtMove)

    #the search failed, return undefined
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    visited = []
    #checking if goal is already met before entering loop
    if problem.isGoalState(start):
        return visited

    exploring = util.Queue()
    exploring.push(start)
    #create dictionaries that can store pacman's movement
    parentPath = {}
    pastMoves = {}

    while not exploring.isEmpty():
        curr = exploring.pop()
        visited.append(curr)
        for (nxtMove, direction, cost) in problem.getSuccessors(curr):
            if nxtMove not in visited:
                #q.append(nxtMove)
                visited.append(nxtMove)
                #record path and direction taken
                parentPath[nxtMove] = curr
                pastMoves[nxtMove] = direction
                if problem.isGoalState(nxtMove):
                    return getPath(nxtMove, parentPath, pastMoves)
                exploring.push(nxtMove)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    start = problem.getStartState()
    visited = []
    #no path to return
    if problem.isGoalState(start):
        return visited

    exploring = util.PriorityQueue()
    #create dictionaries that can record pacman's movement
    parentPath = {}
    pastMoves = {}

    exploring.push(start, 0)
    while not exploring.isEmpty():
        curr = exploring.pop()
        visited.append(curr)
        #same concept as earlier methods
        for (nxtMove, direction, cost) in problem.getSuccessors(curr):
            if nxtMove not in visited:
                visited.append(nxtMove)
                parentPath[nxtMove] = curr
                pastMoves[nxtMove] = direction
                if problem.isGoalState(nxtMove):
                    return getPath(nxtMove, parentPath, pastMoves)
                #check if nxtMove already exists, if it does,
                #update it with new priority
                exploring.update(nxtMove, cost)
    #the search failed. raise undefined
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
    visited = []
    start = problem.getStartState()
    #no path to return
    if problem.isGoalState(start):
        return visited
    #create dictionaries that can record pacman's movement
    parentPath = {}
    pastMoves = {}

    #priority queue with start aka OPEN set
    exploring = util.PriorityQueue()
    exploring.push(start, 0)

    #start expanding nodes!
    while not exploring.isEmpty():
        curr = exploring.pop()
        visited.append(curr)

        for (nxtMove, direction, cost) in problem.getSuccessors(curr):
            if nxtMove not in visited:
                visited.append(nxtMove)
                parentPath[nxtMove] = curr
                pastMoves[nxtMove] = direction
                #update heuristic
                heur = heuristic(nxtMove, problem)
                if problem.isGoalState(nxtMove):
                    return getPath(nxtMove, parentPath, pastMoves)
                #check if nxtMove already exists, if it does,
                #update it with new priority
                exploring.update(nxtMove, cost + heur)

    #search failed, raise not defined
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
