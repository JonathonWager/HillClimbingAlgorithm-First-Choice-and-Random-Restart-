#jonathon Wager
#3/27/2024
#4550 A2 Random-restart hill climbing
import random
import time

#class for nodes that hold a 1d array as a state and a score 
class Node:
    def __init__(self, state, heuristic_score):
        self.state = state
        self.heuristic_score = heuristic_score
#function is given a state and returns the amount of attacking pairs
def conflictScore(state):
    conflicts = 0
    for x in range(8): 
        queenLocation = state[x]
        for y in range(8-x-1):
            #horizontal pairs
            if queenLocation == state[y+x +1]:
                conflicts = conflicts+ 1 
            #diagonal up pairs
            if(queenLocation + y + 1 == state[y+x+1]):
                conflicts = conflicts+ 1 
            #diagonal down pairs
            if(queenLocation - y - 1 == state[y+x+1]):
                conflicts = conflicts + 1 
    return conflicts
#this function creates and returns a random state
def randomState():
    state = [0] * 8
    for x in range(8):
        state[x] = random.randrange(0, 8)  
    return state

#given a node this function generates all possible succsessor states
def findNextState(currentNode):
    bestState = currentNode.state[:]
    bestScore = currentNode.heuristic_score
    foundNextState = False

    for x in range(8):  
        for newPos in range(8):  
            if newPos != currentNode.state[x]:  
                newState = currentNode.state[:]
                newState[x] = newPos
                newScore = conflictScore(newState)
                if newScore < bestScore:
                    bestState = newState
                    bestScore = newScore
                    foundNextState = True
    #if a succsessor was found return it. If not return new random state
    if foundNextState:
        return Node(bestState, bestScore), False
    else:
        return Node(randomState(), conflictScore(bestState)), True
#the algorithm itself
#trys to solve the 8 queen problem in 100 restarts or less
def hillClimb():
    startState = randomState()
    state = Node(startState, conflictScore(startState))
    restarts = 0
    while True:
        if(state.heuristic_score == 0):
            return (state,restarts)
        state = findNextState(state)
        if(state[1]):
            restarts = restarts + 1
            if(restarts >= 100):
                print("Restart Limit Reached")
                return (state[0],restarts)  
        state = state[0]

#get start time
start_time = time.time()

#call algorithm
result = hillClimb()

#get end time
end_time = time.time()
#print results
print(result[0].state)
print(" Restarts= " + str(result[1]))
print(" Attacking Pairs= " + str(result[0].heuristic_score))
#calculate and print total time
total_time = end_time - start_time
print(f"Total time required to reach the final state: {total_time} seconds")