class Dij:
    # matrix of roads
    road = [[]]
    # infinity
    infinit = 9999
    # array of costs
    D = []
    # array of selected nodes
    S = []
    # array of fathers
    T = []
    # number of nodes
    nodes = -1
    # output
    output = []

    def __init__(self, start):
        self.readGraph()
        self.r = start
        r = self.r
        self.S[r] = 1
        for j in range(1, self.nodes + 1):
            self.D[j] = self.road[r][j]
        for j in range(1, self.nodes + 1):
            if self.D[j]:
                self.T[j] = r
        for i in range(1, self.nodes):
            min = 9999
            for j in range(1, self.nodes + 1):
                if self.S[j] == 0:
                    if self.D[j] < min:
                        min = self.D[j]
                        pos = j
            self.S[pos] = 1
            for j in range(1, self.nodes + 1):
                if self.S[j] == 0:
                    if self.D[j] > self.D[pos] + self.road[pos][j]:
                        self.D[j] = self.D[pos] + self.road[pos][j]
                        self.T[j] = pos
        f = open('road.out', 'w')
        for k in range(1, self.nodes + 1):
            if k is not r:
                if self.T[k]:
                    print
                    "Road from ", r, " to ", k
                    self.draw(k)
                    print
                    self.output
                    f.write("Road from {} to {} => {}".format(r, k, str(self.output)))
                    f.write("\n")
                    self.output = []
                else:
                    print
                    "There is not exists road"
        f.close()

    def draw(self, node):
        if self.T[node]:
            self.draw(self.T[node])
        print
        node
        self.output.append(node)

    def readGraph(self):
        counter = 0
        input = []
        with open('example.txt', 'r') as file:
            for a_line in file:
                counter += 1
                if counter == 1:
                    number_of_nodes = int(a_line.rstrip())
                else:
                    input.append(a_line.rstrip())
        size = len(input)
        self.nodes = number_of_nodes
        self.road = [[0 for i in range(0, number_of_nodes + 1)] for j in range(0, number_of_nodes + 1)]
        for i in range(0, self.nodes + 1):
            for j in range(0, self.nodes + 1):
                if i == j:
                    self.road[i][j] = 0
                else:
                    self.road[i][j] = self.infinit
        for i in range(0, size):
            component = input[i]
            node1 = int(component[0])
            node2 = int(component[2])
            cost = int(component[4])
            self.road[node1][node2] = cost

        # init
        self.D = [0] * (number_of_nodes + 1)
        self.S = [0] * (number_of_nodes + 1)
        self.T = [0] * (number_of_nodes + 1)

ob = Dij(2)