import timeit 
import copy 
from networkX_functions import NetworkGenerator

## TO-DO List
# Add argument parser to generate the network without having to alter the file

# initial parameters, can be passed to the NetworkGenerator object ir not 
nodes = 100 
edges = 250 

G = NetworkGenerator() 

start_time_creation = timeit.default_timer() 
G.generate_network() 
#G.print_network() 
print(timeit.default_timer() - start_time_creation) 

H = copy.deepcopy(G) 
I = copy.deepcopy(G) 

start_time_removal = timeit.default_timer() 
G.remove_nodes_and_edges(10) 
#G.print_network() 
print(timeit.default_timer() - start_time_removal) 

start_time_removal = timeit.default_timer() 
H.remove_nodes_and_edges(50) 
#H.print_network() 
print(timeit.default_timer() - start_time_removal) 

start_time_removal = timeit.default_timer() 
I.remove_nodes_and_edges(90) 
#I.print_network() 
print(timeit.default_timer() - start_time_removal)

