from mcstt import *
from huepy import *
g = Graph()
print(lightgreen("""
Minimum Cost Spanning Tree(MCST)  
Developed by KKN,KKW,HHA  
"""))
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                else:
                    print('Edge already exists.')
 
    elif operation == 'mst':
        mst = mst_krusal(g)
        print('Minimum Spanning Tree:')
        mst.display()
        print()
 
    elif operation == 'display':
        g.display()
        print()
 
    elif operation == 'quit':
        break