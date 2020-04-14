import pandas as pd
import numpy as np
from matplotlib.pyplot import show as show_plot

from ..calc.localmag import calculate_local_magnetic_field
from ..config.const import iss_inc, H_eq
from ..config.sim_config import T_MAX, PLOT
from ..util.files import join_path, ROOT_DIR, DATA_FOLDER, LLA_POS_1
from ..util.math import deg2rad
from ..util.plot import plot

# Longitude, latitude and altitude data of satellite
lla_pos = pd.read_csv(
    join_path(ROOT_DIR, DATA_FOLDER, LLA_POS_1),
    sep=',',
    delimiter='\t',
    header=None
)

# Resolution of position data. Number of rows in this case.
pos_resolution = lla_pos.shape[0]

# Time points
orbit_time = np.linspace(0, T_MAX, pos_resolution)

# Latitude and longitude in rad.
orbit_lat = deg2rad(lla_pos.iloc[:,1])
orbit_long = deg2rad(lla_pos.iloc[:,2])

# Calculate the local magnetic field
H, H_mag = calculate_local_magnetic_field(orbit_lat, orbit_long, H_eq, deg2rad(iss_inc))

# Plot local magnetic field strength
plot(np.arange(pos_resolution), H_mag, "Time (s)", "Earth magnetic field strength [T]", "Local magnetic field strength across time")

# Show plots. Include before EOF.
if PLOT:
    show_plot()
