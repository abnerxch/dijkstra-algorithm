# Dijkstra Algorithm
Project made in Algorithm &amp; Complexity class at CS UFM.

Quick and dirty implementation of [Dijkstra's algorithm](http://en.wikipedia.org/wiki/Dijkstra's_algorithm) for finding shortest path distances in a connected graph.

This implementation has a *O((m+n) log n)* running time, where *n* is the number of
vertices and *m* is the number of edges. If the graph is connected (i.e. in one piece), *m* normally dominates over *n*, making the algorithm *O(m log n)* overall.

Dijkstra's algorithm, conceived by computer scientist Edsger Dijkstra, is a graph search algorithm that solves in single-source
shortest path problem for a graph with non-negative edge path costs, producing a shortest path tree. 

![Screenshot](http://farm6.staticflickr.com/5572/15142640541_6ea1eb3d48.jpg)

The `readGraph` function is provided as a convenience:

```python
    counter = 0
        input = []
        with open(example.txt, 'r') as file:
            for a_line in file:
                counter += 1
                if counter == 1:
                    number_of_nodes = int(a_line.rstrip())
                else:
                    input.append(a_line.rstrip())
```
## I want to use this!


First, you have to clone the repository

```shell
git clone https://github.com/abnerxch/dijkstra-algorithm.git
```

Then run the application as follows:

```shell
python dijkstra.py
```

It will generate a `road.out` file where the shortest route (or routes) to reach a particular node is shown

