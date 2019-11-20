from collections import defaultdict
import random
from math import sqrt

nodes_set = set()
edges_set = set()
node_neighbors_dict = {}

# num_initial_spreaders = 2
num_initial_spreaders = [20,40,60,10,100,150,200,1,10]
index = 3
elected_spreaders = set()
longest_shortest_path = 14

with open('t.txt') as inputfile:
  for line in inputfile:
    line=line.strip().split()
    node=[line[0], line[1]]
    weight=int(line[2])
    # print nodes
    node.sort()
    # print nodes
    for n in node:
      nodes_set.add(n)
    edges_set.add(tuple([node[0], node[1], weight]))


num_nodes = len(nodes_set)  #23133
num_edges = len(edges_set)  #93497

neighbors_dict = defaultdict(set)
for (node_0, node_1, weight) in edges_set:
  neighbors_dict[node_0].add((node_1, weight))
  neighbors_dict[node_1].add((node_0, weight))



# average degree of network
average_degree = 0.0
for node, neighbors in neighbors_dict.items():
  average_degree += len(neighbors)


average_degree=float(average_degree)
average_degree /= float(num_nodes)
print("average degree of the graph is :" + str(average_degree))

def vote_and_elect(node_voting_info):
  node_with_max_votes = ""
  max_votes = 0
  for node, voting_info in node_voting_info.items():
    neighbors = neighbors_dict[node]
    num_votes_received = 0
    for neighbor in neighbors:
      num_votes_received += node_voting_info[neighbor[0]][1]*neighbor[1]
    num_votes_received=sqrt(num_votes_received)
    num_votes_received=num_votes_received*sqrt(len(neighbors))
    if num_votes_received > max_votes:
      max_votes = num_votes_received
      node_with_max_votes = node
    node_voting_info[node] = (num_votes_received, node_voting_info[node][1])
  return node_with_max_votes



def update_voting_ability(elected_node, neighbors_dict, node_voting_info, average_degree):
  for neighbor, weight in neighbors_dict[elected_node]:
    new_voting_ability = node_voting_info[neighbor][1] - 1./average_degree
    if new_voting_ability >= 0:
      node_voting_info[neighbor] = (node_voting_info[neighbor][0], new_voting_ability)

      
# initialize the algorithm
# node_voting_info = {}
# for node in nodes_set:
#   node_voting_info[node] = (0, 1) # (number of votes received, voting power)
# while (len(elected_spreaders) < num_initial_spreaders[index]):
#   elected_node = vote_and_elect(node_voting_info)
#   # print(elected_node)
#   elected_spreaders.add(elected_node)
#   node_voting_info[elected_node] = (0, 0)
#   update_voting_ability(elected_node, neighbors_dict, node_voting_info, average_degree)
# print(elected_spreaders)

###################################

# def infection(neighbors_dict, elected_spreaders, infected_bound = num_nodes*0.8, infection_rate = 0.3):
#   infected_set = set(elected_spreaders)
#   newly_infected_set = set()
#   t = 0
#   while len(infected_set) < infected_bound:
#     for infected_node in infected_set:
#       neighbor = random.choice(list(neighbors_dict[infected_node]))
#       if random.uniform(0,1) <= infection_rate:
#         newly_infected_set.add(neighbor)
#     t+=1
#     infected_set = infected_set.union(newly_infected_set)
#   return t

# run infection
import time
a=time.time()
avg = 0
for test in num_initial_spreaders[:1]:
  node_voting_info = {}
  for node in nodes_set:
    node_voting_info[node] = (0, 1) # (number of votes received, voting power)
  print "Selecting "+str(num_initial_spreaders[index])+" spreaders"
  while (len(elected_spreaders) < num_initial_spreaders[index]):
    # print "bla"
    # print "Selected" +str(len(elected_spreaders))
    elected_node = vote_and_elect(node_voting_info)
    # print(elected_node)
    elected_spreaders.add(elected_node)
    node_voting_info[elected_node] = (0, 0)
    update_voting_ability(elected_node, neighbors_dict, node_voting_info, average_degree)


print(elected_spreaders)
print round(time.time()-a,2)


  # for i in range(0,100):
  #   avg+=infection(neighbors_dict, elected_spreaders)
  # print(num_initial_spreaders[index])
  # print("Average # of time steps until convergence: " + str(avg/100))
  # index = index + 1
  # avg = 0
  # elected_spreaders = set()
f=open("output.txt",'a')
for i in elected_spreaders:
  f.write(str(i)+'\n')


# input("bla")












