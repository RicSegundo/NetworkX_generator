import argparse
from networkX_functions import NetworkGenerator

parser = argparse.ArgumentParser(description="Generate a random graph network, if a list of nodes/edges isn't provided")
parser.add_argument("-n", "--nodes", type=int, default=None,
                    help="number of nodes to generate")
parser.add_argument("-e", "--edges", type=int, default=None,
                    help="number of edges to generate")
parser.add_argument("-p", "--percentage", type=int, default=None,
                    help="percentage of edges to remove from the network")
parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True,
                    help="if present, the network structure won't be printed to stdout")

# initial parameters, can be passed to the NetworkGenerator object as arguments, otherwise
# it will run with the predefined values, set in the Class parameters/methods 

args = parser.parse_args()

G = NetworkGenerator(args.nodes, args.edges)

G.generate_network()
G.print_network(args.verbose)

G.remove_nodes_and_edges(args.percentage)
G.print_network(args.verbose)

