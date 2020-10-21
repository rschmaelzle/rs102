#import the NetworkX module with the abbreviation nx
import networkx as nx


# define a network
G_symmetric = nx.Graph()


# add edges (as you do this, nodes are also created)
G_symmetric.add_edge('Peter Miller','Maria Meier')
G_symmetric.add_edge('Peter Miller','Jonathan Franzen')
G_symmetric.add_edge('Hans Fallada','Jonathan Franzen')
G_symmetric.add_edge('Peter Miller','Hans Fallada')
G_symmetric.add_edge('Peter Miller','Kurt Vonnegut')
G_symmetric.add_edge('Maria Meier','Jonathan Franzen')
G_symmetric.add_edge('Maria Meier','Hans Fallada')
G_symmetric.add_edge('Kurt Vonnegut','Jonathan Franzen')

# add an edge between Thomas Mann and Maria Meier
G_symmetric.add_edge('Thomas Mann','Maria Meier')


# plot the network
nx.draw_networkx(G_symmetric)


# measure the degree of Peter Miller
nx.degree(G_symmetric, 'Peter Miller')
