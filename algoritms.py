# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 13:59:00 2022

@author: tunder

Grokking Algorithms by Aditya Bhargava
Done in order to refresh my memory and store them all in one place 
(･ω<)☆
"""

from collections import deque


#binary search ch1
def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    
    while low <= high:
        mid = (low + high)
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else:
            low = mid + 1
    return None 

# find the min in the array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# selection Sort ch2
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# important note: 
# to avoid infinte loop there should be
# a basic clause and a recursion clause
def basic_recursion(i):
    print(f"basic recursion countdown {i}")
    if i < 1:
        return
    else:
        basic_recursion(i-1)
        
        
        
#quick sort         
def qsort(lst):
    if len(lst) < 2:
        return lst

    pivot = lst[0]
    left = list(filter(lambda x: x <= pivot, lst[1:]))
    right = list(filter(lambda x: x > pivot, lst[1:]))
    
    return qsort(left) + [pivot] + qsort(right)
        
# one of the methods to display a graph
# in a code from is to use a dictionary
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
    
#BFS 
def person_is_selling(name):
    return name[-1] == "m"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        # print(search_queue)
        person = search_queue.popleft()
        if not person in searched:
            if person_is_selling(person):
                print(f"{person} is a seller of mangoes!!!")
                return True
            else: 
                search_queue += graph[person]
                searched.append(person)
    
    return False
# dijkstra algorithm (for graphs with weights)
# a way to set up a weighted graph is to use 3 hashmaps
# the grapgh itself, the weight (cost) and  parents

# the graph itself w for weighted
graphw = {}
graphw["start"] = {}
graphw["start"]["a"] = 6
graphw["start"]["b"] = 2
graphw["a"] = {}
graphw["a"]["fin"] = 1
graphw["b"] = {}
graphw["b"]["a"] = 3
graphw["b"]["fin"] = 5
graphw["fin"] = {}

# costs
infinty = float("inf")
costs={}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

#parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#keeping track
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None 
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graphw[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    



my_list = [10, 2, 4, 1, 5, 20]
print("dijkstra algorythm", costs)

print("BFS in graph", search('you'))
print(f"Testing array {my_list}")
print("binary search: ", binary_search(my_list, 1))
print("selection sort (sort from min to max): ", selection_sort(my_list))
print("quick sort", qsort([1, 8, 4, 12, 6, 4, 75]))

basic_recursion(3)

