import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mist/Documents/projects/DroneProject/ws_quadcopter_traj_opt/install/px4_offboard_position'
