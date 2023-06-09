#ideas


# 2 branch a midpoint noot crystals
# 3 if eggs closeby add them to targets
# 4 find all distances during initiation
# 5 find x,y of all cells
# set egg range based on ratio of eggs to crystals
# work out how to minimise time to 51% crystals



import sys

# Python code to sort the tuples using second element
# of sublist Inplace way to sort using sort()
def Sort(sub_li):
 
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[1])
    return sub_li

class Cell(object):
    index: int
    cell_type: int
    resources: int
    neighbors: list[int]
    my_ants: int
    opp_ants: int

    def __init__(self, index: int, cell_type: int = -1, resources: int = 0, neighbors: list[int] = [], my_ants: int = 0, opp_ants: int = 0,x :int =-1, y : int=-1):
        self.index = index
        self.cell_type = cell_type
        self.resources = resources
        self.neighbors = neighbors
        self.my_ants = my_ants
        self.opp_ants = opp_ants
        self.x = x
        self.y = y



class path_node():
    def __init__(self,cell : int,parent : int,step : int):
        self.cell = cell
        self.parent = parent
        self.step = step

# list of crystal and egg cells    
def target_cells():
    targets =[]
    for c in cells:
        if c.resources > 0:
            targets.append(c.index)
    return targets
    

def cells_in_order(cells,type):
    crystal_cells = []
    for cell in cells:
        for b in my_bases:
            if cell.cell_type == type and cell.resources > 0 :
                dist = distance(cells[b],cell)
                crystal_cells.append([cell.index,dist,b])

    return Sort(crystal_cells)

#create a 2d list of distances between cells
def distance_map():
    distances = []
    for i in range(len(cells)):
        cd = []
        for j in range(len(cells)):
            cd.append(index_distance(i,j))
        distances.append(cd)
        #print(cd, file=sys.stderr, flush=True)
    return distances
    
def path_strength(source : int):
    end_strength = 0
    queue = [[source,cells[source].my_ants]]
    explored = []
    
    found_end= False
    if cells[source].my_ants == 0:
        #no ants at the start so cant send crystals
        end_strength = 0
        found_end = True
    while queue:
        print("queue =: "+str(queue), file=sys.stderr, flush=True)
        next_cell = queue.pop(0)
        explored.append(next_cell[0])
        for n in cells[next_cell[0]].neighbors:
            duplicate = False
            if len(queue) >0:
                for i in queue:
                    if i[0] == n: duplicate = True
            if (cells[n].my_ants>0) and (n not in explored) and not duplicate:
                queue.append([n,min(next_cell[1],cells[n].my_ants)])
                print(str(n)+" my_bases: "+str(my_bases), file=sys.stderr, flush=True)
                if n in my_bases: 
                    end_strength = queue[-1][1]
                    found_end = True
                if found_end == True: break
        if found_end == True: break
    print("queue =: "+str(queue), file=sys.stderr, flush=True)
    return end_strength

def best_path(cellA,cellB):
    end_found = False
    path = []
    queue =[]
    explored = []
    # queue includes cell, distance from start and parent
    queue.append([cellA,0,-1])
    while queue:
        next_cell = queue.pop(0)
        explored.append(next_cell)
        for n in cells[next_cell[0]].neighbors:
            in_queue = False
            in_explored = False
            if len(queue)>0:
                for i in queue:
                    if i[0] ==n: in_queue = True
                for j in explored:
                    if j[0] == n: in_explored = True
            if not in_explored and not in_queue:
                queue.append([n,next_cell[1]+1,next_cell[0]])
            if n == cellB:
                end_found = True
            if end_found == True:break
        if end_found == True:break
    if end_found:
        current_cell = queue[-1][0]
        path.append(current_cell)
        next_cell = queue[-1][2]
        print("explored :"+str(explored), file=sys.stderr, flush=True)
        for i in range(queue[-1][1]):
            path.append(next_cell)
            for j in range(len(explored)):
                if explored[j][0] == next_cell:
                    next_cell = explored[j][2]
    return path


def distance(cellA,cellB):
    #print(cellB.index, file=sys.stderr, flush=True)
    path : list[path_node]=[]
    possibles : list[int]=[]
    n=0
    possibles.append(cellA.index)
    path.append(path_node(cellA.index,-1,n))
    found_path = 0
    while not found_path:
        for node in path:
            #print(cells[node.cell].neighbors, file=sys.stderr, flush=True)
            if found_path: break
            for neighbor in cells[node.cell].neighbors:
                #print(neighbor, file=sys.stderr, flush=True)
                if neighbor == cellB.index:
                    #print("break at " + str(n), file=sys.stderr, flush=True)
                    #found the end
                    found_path = True
                    step = node.step+1
                    break
                if neighbor not in possibles:
                    path.append(path_node(neighbor,node.cell,node.step+1))
                    possibles.append(neighbor)
               
    return step


# return the length of the shortest path between to cells
def index_distance(cellA: int,cellB: int):
    #print(cellB.index, file=sys.stderr, flush=True)
    path : list[path_node]=[]
    possibles : list[int]=[]
    n=0
    possibles.append(cellA)
    path.append(path_node(cellA,-1,n))
    found_path = 0
    step = 0
    if cellA == cellB: 
        found_path = 1
    while not found_path:
        for node in path:
            #print(cells[node.cell].neighbors, file=sys.stderr, flush=True)
            if found_path: break
            for neighbor in cells[node.cell].neighbors:
                #print(neighbor, file=sys.stderr, flush=True)
                if neighbor == cellB:
                    #print("break at " + str(n), file=sys.stderr, flush=True)
                    #found the end
                    found_path = True
                    step = node.step+1
                    break
                if neighbor not in possibles:
                    path.append(path_node(neighbor,node.cell,node.step+1))
                    possibles.append(neighbor)
               
    return step

# initialise game and variables
cells: list[Cell] = []
total_crystals = 0
total_eggs = 0
game_turn = 0
collected_crystals = 0

number_of_cells = int(input())  # amount of hexagonal cells in this map



for i in range(number_of_cells):
    # create a cell for each cell on the map
    cell: Cell = Cell(index = i)
    cells.append(cell)

cells[0].x = 0
cells[0].y = 0

for i in range(number_of_cells):
    inputs = [int(j) for j in input().split()]
    cell_type = inputs[0] # 0 for empty, 1 for eggs, 2 for crystal
    initial_resources = inputs[1] # the initial amount of eggs/crystals on this cell
    neigh_0 = inputs[2] # the index of the neighbouring cell for each direction
    neigh_1 = inputs[3]
    neigh_2 = inputs[4]
    neigh_3 = inputs[5]
    neigh_4 = inputs[6]
    neigh_5 = inputs[7]
    
    
    cells[i].cell_type = cell_type
    cells[i].resources = initial_resources
    cells[i].neighbors = list(filter(lambda id: id > -1,[neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]))

number_of_bases = int(input())
my_bases: list[int] = []
for i in input().split():
    my_base_index = int(i)
    my_bases.append(my_base_index)
opp_bases: list[int] = []
for i in input().split():
    opp_base_index = int(i)
    opp_bases.append(opp_base_index)
targets = []

dmap = distance_map()
#print(dmap, file=sys.stderr, flush=True)
print("path 27-->28 : "+str(best_path(27,28)), file=sys.stderr, flush=True)
print("starting game loop", file=sys.stderr, flush=True)
# game loop
while True:
    game_turn += 1
    #game loop initiation
    total_crystals = 0
    targeted_crystals = 0
    
    total_eggs = 0
    my_total_ants = 0
    egg_weight = 1
    crystal_weight = 1
    crystal_target_ratio = 0.7
    egg_range = 2
    for i in range(number_of_cells):
        inputs = [int(j) for j in input().split()]
        resources = inputs[0] # the current amount of eggs/crystals on this cell
        my_ants = inputs[1] # the amount of your ants on this cell
        opp_ants = inputs[2] # the amount of opponent ants on this cell

        cells[i].resources = resources
        cells[i].my_ants = my_ants
        my_total_ants += my_ants
        cells[i].opp_ants = opp_ants
        if cells[i].cell_type == 1:
            total_eggs += resources
        if cells[i].cell_type == 2:
            total_crystals += resources

    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    actions = []
    lines = []
    linked = []
    total_lines = 0
    targetted_crystal = 0
    print("adding nearby eggs", file=sys.stderr, flush=True)
    # add eggs if within egg_range from base
    
    for b in my_bases:
        egg_targets = cells_in_order(cells,1)
        for t in egg_targets:
            if total_lines >= my_total_ants: break
            if dmap[t[0]][b]<= egg_range:
                lines.append([t[0],b,egg_weight])
                linked.append(t[0])
                total_lines += dmap[t[0]][b]*egg_weight
                

    # add crystal targets

    #add bases to linkedlist
    for i in my_bases:
        linked.append(i)

    
    # get list of targets in order of distance from one of my bases
    
    #list of all possible targets - eggs and crystals
    target_list = target_cells()
    print("Target list.:"+str(target_list), file=sys.stderr, flush=True)

    
    # build lines to the targets based on their distance to the existing lines
    while len(target_list) >0:
        closest = 100000
        closest_link = -1
        closest_target = -1
        for t in target_list:
            for l in linked:
                d = dmap[t][l]
                if d<closest:
                    if cells[t].cell_type == 1 and d>egg_range:
                        pass
                    else:
                        closest = d
                        closest_link = l
                        closest_target = t
        if total_lines + closest >= my_total_ants: break
        total_lines += closest
        if cells[closest_target].cell_type == 2:
            targetted_crystal += cells[closest_target].resources
        #print("Target size.:"+str(targetted_crystal), file=sys.stderr, flush=True)
        lines.append([closest_target,closest_link,crystal_weight])
        linked.append(closest_target)
        target_list.remove(closest_target)
        if targetted_crystal / total_crystals > crystal_target_ratio: break
    #print("Final Target size.:"+str(targetted_crystal), file=sys.stderr, flush=True)
    

        
    #print("stregth from cell 27: "+str(path_strength(27)), file=sys.stderr, flush=True)        

    for c in cells_in_order(cells,2):
        collected_crystals += path_strength(c[0])
    actions.append("MESSAGE "+str(collected_crystals))
# add targets to output
    beacons =[]
    for line in lines:
        beacons.extend(best_path(line[0],line[1]))
        print("beacons.:"+str(beacons), file=sys.stderr, flush=True)
    for b in beacons:
        actions.append("BEACON "+str(b)+" 1")

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(actions) == 0:
        print('WAIT')
    else:
        print(';'.join(actions))
