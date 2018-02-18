# module to account for inertia properties of rigid bodies

# some constants
_zvec = [0,0,0]
_z3x3 = [[0,0,0],[0,0,0],[0,0,0]]
_e3x3 = [[1,0,0],[0,1,0],[0,0,1]]


class _body(object):
    """
    """
    def __init__(self, name=None, m=0, I=_z3x3, T=_e3x3, r_cg=_zvec, r_rk=_zvec):
        self.name = name
        self.mass_cgk = m
        self.I_Bk_rk_Rk = I
        self.T_R_Rk = T
        self.r_cgk_rk_RK = r_cg
        self.r_rk_r_R = r_rk
    def __add__(self, other):
        total_mass = self.mass_cgk + other.mass_cgk
        return _body(m=total_mass)
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    def _get_args(self):
        return {'name':self.name, \
                'm':self.mass_cgk, \
                'I':self.I_Bk_rk_Rk, \
                'T':self.T_R_Rk, \
                'r_cg':self.r_cgk_rk_RK, \
                'r_rk':self.r_rk_r_R}
        
        
class body(_body):
    def __init__(self, **args):
        super(body, self).__init__(**args)
        self.sub_bodies = [_body(**args)]
    def __add__(self, other):
        all_bodies = self.sub_bodies + other.sub_bodies
        new_body = body(**sum(all_bodies)._get_args())
        new_body.sub_bodies = all_bodies
        return new_body


if __name__ == '__main__':
    # example to add a bunch of bodies
    b1 = body(m=11)
    b2 = body(m=22)
    b3 = body(m=33)
    b4 = body(m=44)
    b = sum([b1,b2,b3,b4])
    print b.mass_cgk