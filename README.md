# UE4Poly

This python module is meant to connect to an UE4 game which is running a MessagePack RPC Server for drawing Polygons.  The UE4 MessagePack server is installed seperately as a plugin and be found [here](https://github.com/JeremyBYU/UE4PolygonServer). This python client and UE4 plugin combination allows you to draw polygons into the environment.

Examples can be found in the `examples` folder.

## How to use

Polygons have the same verbage as Shapely. Namely a Polygon has a required outer **shell** that is a closed LinearRing. Also a polgyon may have 0 or more LinearRing **holes** that are inside the polygon

```python
import numpy as np
from ue4poly import UE4Poly
from ue4poly.types import DPCommand
def main():
    poly_client = UE4Poly(port=3000)
    poly_client.ping() # Just to make sure that commmand are being recieved

    # Construct a square that has side lenght 200
    shell_np = np.array([
            [0.0, 0.0, 0.0], 
            [200.0, 0.0, 0.0], 
            [200.0, 200.0, 0.0],
            [0.0, 200.0, 0.0]])

    # Flatten the to python list
    shell = shell_np.flatten().tolist()
    # Create an *optional* smaller square hole insize the square polygon
    hole = (shell_np * 0.25 + [50, 50, 0]).flatten().tolist()
    
    cmd = DPCommand(lifetime=5.0, shell=shell, holes=[hole],thickness=4.0)
    poly_client.draw_polygon(cmd)

if __name__ == "__main__":
    main()

```