# hello.py
print('hello Git!')

import numpy as np
np.random.seed (1)
x0 = np.random.normal (2, 0.45, 300)
y0 = np.random.normal (2,0.45, 300)

x1 = np.random.normal (6, 0.4, 200)
y1 = np.random.normal (6, 0.4, 200)

x2= np.random.normal (4, 0.3, 200)
y2 = np.random.normal (4, 0.3, 200)

#create figure
fig = go.Figure ()

# Add scatter traces
fig.add_ trace (go.Scatter(
  x= x0
  y= y0
  mode = "markers", ))

fig.add_trace(go.Scatter (
  x= x1
  y= y1
  mode = "markers"))

figure.add_trace (go.Scatter (
  x= x2
  y= y2
  mode = "markers"))

fig.add_trace (go.Scatter ( 
  x= x2
  y= y2
  mode = "markers" ))

fig.add_trace (go.Scatter (
  x= x1
  y= y0
  mode = "markers"))

# Add shapes
fig.update_layout (
  shapes = [
    direct (
      type = "circle", 
      xref = "y", 
      x0 = min(x0),
      y0 = min (y0),
      x1 = max (x0),
      y1 = max (y0),
      opacity = 0.2
      fillcolor = "cyan", 
      line_color = "blue", ), 
    
    dict (
      type = "circle", 
      xref = "x", 
      yref = "y", 
      x0 = min (x1),
      y0 = min (y1), 
      x1 = max (x1),
      y1 = max (y1),
      opacity = 0.2, 
      fillcolor = "orange", 
      line_color = "orange", ),
    
    dict (
      type = "circle", 
      xref = "x", 
      yref = "y", 
      x0 = min (x2), 
      y0 = min (y2), 
      x1 = max (x2), 
      y1 = max (y2), 
      opacity = 0.2, 
      fillcolor = "green", 
      line_color = "green", ), 
    
   
    dict (
      type = "circle", 
      xref = "x", 
      yref = "y", 
      x0 = min (x2), 
      y0 = min (y2), 
      x1 = max (x2), 
      y1 = max (y2), 
      opacity = 0.2, 
      fillcolor = "red", 
      line_color = "red", ), 
  ].
)
# Hide legend
fig.update_ layout (showlenged = False) 
fig.show ()
    
      
