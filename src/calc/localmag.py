from numpy import sin, cos, zeros
from numpy.linalg import norm

def calculate_local_magnetic_field(latitude, longitude, H_eq, inclination):
    '''
    Calculate the magnitude of local magnetic field.
    '''
    # Check latitude and longitude data length
    data_length = len(latitude)
    if (len(longitude) != data_length):
        raise Exception("Data misalignment for latitude and longitude")
    
    # Initialize magnetic field strength matrix
    H = zeros((data_length, 3))
    H_mag = zeros(data_length)

    # Calculation of local magnetic field strength
    # Reference: D.T.Gerhardt
    for i in range(data_length):
        # Vector
        H[i][0] = 3 * H_eq * sin(inclination) * cos(inclination) * sin(latitude[i])**2
        H[i][1] = -3 * H_eq * sin(inclination) * sin(latitude[i]) * cos(latitude[i])
        H[i][2] = H_eq * ( 1 - 3 * sin(inclination)**2 * sin(latitude[i])**2 )
        
        # Magnitude
        H_mag[i] = norm(H[i])

    return H, H_mag 