from ue4poly import UE4Poly
from ue4poly.types import DPCommand
def main():
    poly_client = UE4Poly()
    poly_client.ping()
    cmd = DPCommand(lifetime=-1.0, shell=[1.0, 2.0, 3.0, 4.0], color=[100, 10, 13])
    poly_client.draw_polygon(cmd)

if __name__ == "__main__":
    main()