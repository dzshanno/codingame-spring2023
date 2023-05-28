import sys



class Cell(object):
    index: int
    cell_type: int
    resources: int
    neighbors: list[int]
    my_ants: int
    opp_ants: int

    def __init__(self, index: int, cell_type: int, resources: int, neighbors: list[int], my_ants: int, opp_ants: int,x :int =-1, y : int=-1):
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

def build_map():
    pass

def distance(cellA,cellB):
    print(cellB.index, file=sys.stderr, flush=True)
    path : list[path_node]=[]
    possibles : list[int]=[]
    n=0
    possibles.append(cellA.index)
    path.append(path_node(cellA.index,-1,n))
    found_path = 0
    while not found_path:
        for node in path:
            print(cells[node.cell].neighbors, file=sys.stderr, flush=True)
            if found_path: break
            for neighbor in cells[node.cell].neighbors:
                print(neighbor, file=sys.stderr, flush=True)
                if neighbor == cellB.index:
                    print("break at " + str(n), file=sys.stderr, flush=True)
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
    inputs = [int(j) for j in input().split()]
    cell_type = inputs[0] # 0 for empty, 1 for eggs, 2 for crystal
    initial_resources = inputs[1] # the initial amount of eggs/crystals on this cell
    neigh_0 = inputs[2] # the index of the neighbouring cell for each direction
    neigh_1 = inputs[3]
    neigh_2 = inputs[4]
    neigh_3 = inputs[5]
    neigh_4 = inputs[6]
    neigh_5 = inputs[7]
    cell: Cell = Cell(
        index = i,
        cell_type = cell_type,
        resources = initial_resources,
        neighbors = list(filter(lambda id: id > -1,[neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5])),
        my_ants = 0,
        opp_ants = 0
    )
    cells.append(cell)
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
    strategy = 1

    if strategy ==1:
        # if more crystals than eggs go for eggs
        target_type = 2
        if total_crystals > total_eggs:
            target_type = 1
        if total_crystals < total_eggs:
            target_type = 2
        if total_crystals == 0:
            target_type = 1
        if total_eggs == 0:
            target_type = 2

        # go after some crystals
        targets.append(richest_cell(cells,2))


        if richest_cell(cells,target_type) not in targets:
            targets.append(richest_cell(cells,target_type))

    if strategy == 2:
        #start from closest
        closest = 100000
        closest_cell = None
        for i in cells:
            if (distance(cells[my_bases[0]],i)< closest) and (i.resources >0):
                closest_cell = i
                closest = distance(cells[my_bases[0]],i)
        targets.append(closest_cell)

    if strategy == 3:
        #everything everywhere all at once
        for i in cells:
            targets.append(i)

    for i,target in enumerate(targets):
        if target.resources == 0:
            targets.pop(i)

    for target in targets:
            actions.append("LINE "+str(my_bases[0])+" "+str(target.index)+" 1")


    # TODO: choose actions to perform and push them into actions
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(actions) == 0:
        print('WAIT')
    else:
        print(';'.join(actions))
