import matplotlib.pyplot as plt
from ..config.sim_config import PLOT

def plot(x, y, x_label=None, y_label=None, title=None):
    
    if(PLOT):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x,y)
        
        if title:
            ax.set_title(title)
        
        if x_label:
            ax.set_xlabel(x_label)
        
        if y_label:
            ax.set_ylabel(y_label)
