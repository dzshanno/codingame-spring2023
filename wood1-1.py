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

def richest_cell(cells,cell_type):
    max_resources = -1
    for i in cells:
        if (i.cell_type == cell_type and i.resources > max_resources):
            richest = i
    return richest

def cells_in_order(cells,type):
    crystal_cells = []
    for cell in cells:
        for b in my_bases:
            if cell.cell_type == type and cell.resources > 0 :
                dist = distance(cells[b],cell)
                crystal_cells.append([cell.index,dist,b])

    return Sort(crystal_cells)

def add_xy(ref: int,dir : int ,result: int):
    # set x and y values. x is distance in 0 direction. y is distance in 1 direction
    
    # not working during inititation as no guarentee cells are shown in order
    if neigh_0 != -1:
        cells[neigh_0].x = cells[i].x + 1
        cells[neigh_0].y = cells[i].y
    
    if neigh_1 != -1:
        cells[neigh_1].x = cells[i].x
        cells[neigh_1].y = cells[i].y + 1
    
    if neigh_2 != -1:
        cells[neigh_2].x = cells[i].x - 1
        cells[neigh_2].y = cells[i].y + 1
    
    if neigh_3 != -1:
        cells[neigh_3].x = cells[i].x - 1
        cells[neigh_3].y = cells[i].y

    if neigh_4 != -1:
        cells[neigh_4].x = cells[i].x 
        cells[neigh_4].y = cells[i].y -1
    
    if neigh_5 != -1:
        cells[neigh_5].x = cells[i].x + 1
        cells[neigh_5].y = cells[i].y - 1
            

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

# initialise game and variables
cells: list[Cell] = []
total_crystals = 0
total_eggs = 0


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

# game loop
while True:
    
    #game loop initiation
    total_crystals = 0
    total_eggs = 0
    my_total_ants = 0
    egg_weight = 1
    crystal_weight = 1
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

    # add eggs if within egg_range from base
    egg_range = 3
    for b in my_bases:
        egg_targets = cells_in_order(cells,1)
        for t in egg_targets:
            if total_lines >= my_total_ants: break
            if distance(cells[t[0]],cells[b])<= egg_range:
                lines.append([t[0],b,egg_weight])
                linked.append(t[0])
                total_lines += distance(cells[t[0]],cells[b])*egg_weight

    # add crystal targets
    possible_targets = cells_in_order(cells,2)
    print("possible targets=" + str(possible_targets), file=sys.stderr, flush=True)
    lines.append([possible_targets[0][2],possible_targets[0][0],crystal_weight])
    total_lines += possible_targets[0][1]*crystal_weight
    print("total lines=" + str(total_lines), file=sys.stderr, flush=True)
    linked.append(possible_targets[0][0])
    linked.append(possible_targets[0][2])
    for n in cells[possible_targets[0][2]].neighbors:
            if cells[n].cell_type == 1 and cells[n].resources>0:
                lines.append([n,possible_targets[0][2],crystal_weight])
                total_lines +=1*egg_weight

    for n in cells[possible_targets[0][0]].neighbors:
            if cells[n].cell_type == 1 and cells[n].resources>0:
                lines.append([n,possible_targets[0][0],crystal_weight])
                total_lines +=1*egg_weight

    possible_targets.pop(0)
    
    for t in possible_targets:
        
        closest = 100000
        closest_link = -1
        for l in linked:
            d = distance(cells[t[0]],cells[l])
            if d<closest:
                closest = d
                closest_link = l
        total_lines += closest*crystal_weight
    
        
    # add any adjacent eggs
        for n in cells[t[0]].neighbors:
            if total_lines >= my_total_ants: break
            if cells[n].cell_type == 1 and cells[n].resources>0:
                lines.append([n,t[0],crystal_weight])
                total_lines +=1 * crystal_weight

        if total_lines >= my_total_ants: break
        lines.append([t[0],closest_link,crystal_weight])
        linked.append(t[0])
            
    




# add targets to output
    for line in lines:
            actions.append("LINE "+str(line[0])+" "+str(line[1])+" "+str(line[2]))

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(actions) == 0:
        print('WAIT')
    else:
        print(';'.join(actions))
