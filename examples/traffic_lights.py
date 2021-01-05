#!/usr/bin/env python
# traffic_lights.py - http://www.graphviz.org/content/traffic_lights

from graphviz import Digraph

t = Digraph('TrafficLights', filename='traffic_lights.gv', engine='neato')

t.attr('node', shape='box')
for i in (2, 1):
    t.node(f'gy{i:d}')
    t.node(f'yr{i:d}')
    t.node(f'rg{i:d}')

t.attr('node', shape='circle', fixedsize='true', width='0.9')
for i in (2, 1):
    t.node(f'green{i:d}')
    t.node(f'yellow{i:d}')
    t.node(f'red{i:d}')
    t.node(f'safe{i:d}')

for i, j in [(2, 1), (1, 2)]:
    t.edge(f'gy{i:d}', f'yellow{i:d}')
    t.edge(f'rg{i:d}', f'green{i:d}')
    t.edge(f'yr{i:d}', f'safe{i:d}')
    t.edge(f'yr{i:d}', f'red{i:d}')
    t.edge(f'safe{i:d}', f'rg{i:d}')
    t.edge(f'green{i:d}', f'gy{i:d}')
    t.edge(f'yellow{i:d}', f'yr{i:d}')
    t.edge(f'red{i:d}', f'rg{i:d}')

t.attr(overlap='false')
t.attr(label=r'PetriNet Model TrafficLights\n'
             r'Extracted from ConceptBase and layed out by Graphviz')
t.attr(fontsize='12')

t.view()
