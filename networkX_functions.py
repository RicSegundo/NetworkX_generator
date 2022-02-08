import random 
from typing import List 
import networkx as nx 
import matplotlib.pyplot as plt 


class NetworkGenerator(): 
    """Generates a networkX object with an optionally defined number of nodes (otherwise random). 
    The edges between these nodes are also randomly generated. The number of edges can be passed as an argument 
    or will otherwise be 1.5 times the number of nodes. 
    Lists can also be provided, e.g. a list of nodes and/or a list of edges. A list of edges can be provided without 
    the list of nodes. If only providing the list of nodes, the list of edges will be randomly generated and will 
    contain 1.5 times the length of the list of nodes. 

    [Args]: 
    nr_nodes (int) [optional]: number of nodes to initiate the network with. 
    If left empty, will be a random number between 100 and 200 
    nr_edges (int) [optional]: number of edges to initiate the network with. 
    If left empty, will be 1.5 times the number of nodes 
    nodes (List) [optional]: Specific List of nodes, if one does not wants a random generated set 
    edges (List[Tuple]) [optional]: Specific List of tuples containing all the connections between nodes 
    If left empty, will be randomly generated from the nodes list that was passed or in the absence of this 
    will be generated from the randomly generated node list 

    """ 

    def __init__(self, nr_nodes:int = None, nr_edges:int = None, nodes:List = None, edges:List = None): 
        self.network = nx.Graph() 
        self.nr_nodes = nr_nodes 
        self.nr_edges = nr_edges 
        if nodes == None: 
            self.nodes = [] 
        else: 
            self.nodes = nodes 
        if edges == None: 
            self.edges = [] 
        else: 
            self.edges = edges 


    def generate_network(self) -> None: 
        if self.nr_nodes == None and not self.nodes and not self.edges: 
            self.nr_nodes = random.randrange(100,200) 
        if self.nodes: 
            self.nr_nodes = len(self.nodes) 
        if self.nr_edges == None and not self.edges: 
            self.nr_edges = int(self.nr_nodes * 1.5) 
        if not self.nodes and not self.edges: 
            self.nodes.extend([number for number in range(1, self.nr_nodes + 1)]) 
            self.network.add_nodes_from(self.nodes) 
        if not self.edges: 
            self.edges.extend(set(list([tuple(random.sample(self.nodes, 2)) for _ in range(self.nr_edges)]))) 

        self.network.add_edges_from(self.edges) 

    def remove_nodes_and_edges(self, percentage:int) -> None: 
        """ Will remove a certain % of the edges from the graph. 
        Isolated nodes will also be deleted afterwards. 

        [Args]: 
        percentage (int): percentage of the edges to be removed from the graph
        If left empty, the default value is 20
        """ 
        if percentage == None:
            percentage = 20

        edges_to_remove = random.sample(self.edges, (int(len(self.edges) * (percentage/100)))) 
        self.network.remove_edges_from(edges_to_remove) 

        nodes_to_remove = list(nx.isolates(self.network)) 
        self.network.remove_nodes_from(nodes_to_remove) 

    def print_network(self, action:bool) -> None: 
        if action:
            nx.draw(self.network, with_labels=True, font_weight='bold') 
            plt.show() 
            plt.clf() 
