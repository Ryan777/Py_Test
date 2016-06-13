#coding=utf-8
import Tkinter as tk
import networkx as nx
from networkx_viewer import NodeToken, GraphCanvas

class CustomNodeToken(NodeToken):
    def render(self, data, node_name):
        """Example of custom Node Token
        Draw a circle if the node's data says we are a circle, otherwise
        draw us as a rectangle.  Also, if data contains a color key,
        use that as our color (default, red)
        """
        # For our convenience, the render method is called with the
        #  graph's data attributes and the name of the node in the graph

        # Note that NodeToken is a subclass of Tkinter.Canvas, so we
        #  simply draw on ourselves to create the apperance for the node.

        # Make us 50 pixles big
        self.config(width=50, height=50)

        # Set color and other options
        marker_options = {'fill':       data.get('color','red'),
                          'outline':    'black'}

        # Draw circle or square, depending on what the node said to do
        if data.get('circle', None):
            self.create_oval(0,0,50,50, **marker_options)
        else:
            self.create_rectangle(0,0,50,50, **marker_options)

class ExampleApp(tk.Tk):
    def __init__(self, graph, **kwargs):
        tk.Tk.__init__(self)

        self.canvas = GraphCanvas(graph, NodeTokenClass=CustomNodeToken,
            **kwargs)
        self.canvas.grid(row=0, column=0, sticky='NESW')

G = nx.path_graph(5)
G.node[2]['circle'] = True
G.node[3]['color'] = 'blue'

app = ExampleApp(G)
app.mainloop()