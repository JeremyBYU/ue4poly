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