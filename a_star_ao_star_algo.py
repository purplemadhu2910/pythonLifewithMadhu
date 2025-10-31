import heapq

heuristic={
    'a':5,
    'b':4,
    'c':2,
    'd':1,
    'e':0
    }

graph={
       'a':[('b',1),('c',2)],
       'b':[('c',1),('d',2)],
       'c':[('d',1),('e',2)],
       'd':[('e',1)],
       'e':[]
       }

#A* Algorithm

def a_star(start,goal):
    open_list=[]
    heapq.heappush(open_list,(heuristic[start],0,start,[]))
    
    while open_list:
        f,g,current,path=heapq.heappop(open_list)
    
    if current==goal:
        return path,g
    
    for neighbor,cost in graph.get(current,[]):
        g_new=g+cost
        f_new=g_new+heuristic[neighbor]
        heapq.heappush(open_list,(f_new,g_new,neighbor,path))
        
    return None,float('inf')



#AO* Algorithm

def ao_star(state,goal,memo={}):
    if state==goal:
        return [state],0
    
    if state in memo:
        return [state],0
    
    best_path=None
    best_cost=float('inf')
    
    for neighbor,cost in graph.get(state,[]):
        sub_path,sub_cost=ao_star(neighbor,goal,memo)
        total_cost=cost+sub_cost
        
        if total_cost<best_cost:
            best_cost=total_cost
            best_path=[state]+sub_path
            
        memo[state]=(best_path,best_cost)
        return memo[state]
    
if __name__ == "__main__":
    print("Available states: ",list(graph.keys()))
    
    start=input("Enter the START state: ").lower().strip()
    goal=input("Enter the GOAL state: ").lower().strip()
    
    if start not in graph or goal not in graph:
        print("Invalid start or goal state.")
        
    else:
        print("\nUsing A* Search: ")
        path,cost=a_star(start,goal)
        print(f'Path: {path}')
        print(f'Total Cost: {cost}')
        
        
        print("\nUsing AO* Search: ")
        ao_path,ao_cost=(start,goal)
        print(f'Path: {ao_path}')
        print(f'Total Cost: {ao_cost}')

