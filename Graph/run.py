
from CreateGraph import Graph

if __name__ == '__main__':
	g = Graph()
	g.add_vertex('a')
	g.add_vertex('b')
	g.add_vertex('c')
	g.add_vertex('d')
	g.add_vertex('e')

	g.add_edge('c', 'a', 4)
	g.add_edge('c', 'b', 5)
	g.add_edge('c', 'e', 1)
	g.add_edge('c', 'd')
	g.add_edge('b', 'a', 8)
	g.add_edge('b', 'e', 10)

	for v in g:
		for w in v.get_connections():
			vid = v.id
			wid = w.id
			print(vid, wid, v.get_weight(w))

	for v in g:
		print(g.vert_dict[v.get_id()])
