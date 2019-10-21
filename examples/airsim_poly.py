import time
import numpy as np
import airsim
from polylidar import extractPolygons
from polylidarutil import convert_to_shapely_polygons

from ue4poly import UE4Poly
from ue4poly.types import DPCommand

def parse_lidar_data(data):
    # reshape array of floats to array of [X,Y,Z]
    try:
        points = np.array(data.point_cloud, dtype=np.dtype("f4"))
        points = np.reshape(points, (int(points.shape[0] / 3), 3))
        return points
    except:
        return None

def convert_to_ue4(points, scale=100.0, ue4_origin=[0,0,0]):
    """
    Converts NX3 Numpy Array in AirSim NED frame to a flattened UE4 frame 
    """
    points = points * scale # meters to cm
    points[:,-1] = -points[:,-1] # AirSim NED z axis is inverted
    points = points + ue4_origin # Shift to true unreal origin
    points = points.flatten().tolist() # Flatten data, return list for msgpack
    return points

def shapely_to_lr_list(poly, scale=100.0, ue4_origin=[0,0,0]):
    shapely_list = dict(shell=convert_to_ue4(np.array(poly.exterior), scale=scale, ue4_origin=ue4_origin))
    holes = []
    for hole in poly.interiors:
        holes.append(convert_to_ue4(np.array(hole), scale=scale, ue4_origin=ue4_origin))
    shapely_list['holes'] = holes
    return shapely_list

def draw_pc_poly(client, poly_client, ue4_origin=[0,0,0], lifetime=5.0, polylidar_kwargs=dict(alpha=0.0, lmax=2.0, zThresh=0.1)):
    lidar_data = client.getLidarData()
    pc = parse_lidar_data(lidar_data)
    if pc is None:
        return
    try:
        polygons = extractPolygons(pc, **polylidar_kwargs)
    except:
        print("Error using Polylidar")
        polygons = []
    if len(polygons) > 0:
        polygon_shapely = convert_to_shapely_polygons(polygons, pc, return_first=True, sort=True)
        lr_list = shapely_to_lr_list(polygon_shapely, ue4_origin=ue4_origin)

        cmd = DPCommand(lifetime=lifetime, shell=lr_list['shell'], holes=lr_list['holes'],thickness=8.0)
        poly_client.draw_polygon(cmd)


def main():
    client = airsim.MultirotorClient()
    client.confirmConnection()
    # client.enableApiControl(True)
    # client.armDisarm(True)

    poly_client = UE4Poly(port=3000)

    # client.takeoffAsync().join()
    rate = 0.25
    ue4_origin = [1490, -1120.0, 2590]
    while True:
        draw_pc_poly(client, poly_client, ue4_origin=ue4_origin, lifetime=rate)
        time.sleep(rate)



if __name__ == "__main__":
    main()
