max_pos_dict = {'GK':2, 'Def':5, 'Mid':5, 'Atk':3}

class PlayerPort(squad):
    """ PlayerPort class constructs the FF squad through time.
        Used in conjunction with the optimiser class.
    """
    
    def __init__(self, squad):
        self.squad = squad
        
    def FirstXI(self):
        """ """
        return XI_dict