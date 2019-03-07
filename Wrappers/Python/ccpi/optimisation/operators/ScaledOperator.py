from ccpi.optimisation.operators import LinearOperator
from numbers import Number

class ScaledOperator(LinearOperator):
    '''ScaledOperator

    A class to represent the scalar multiplication of an Operator with a scalar. 
    It holds an operator and a scalar. Basically it returns the multiplication
    of the result of direct and adjoint of the operator with the scalar.
    For the rest it behaves like the operator it holds.

    Args:
       operator (Operator): a Operator or LinearOperator
       scalar (Number): a scalar multiplier
    Example:
       The scaled operator behaves like the following:
       sop = ScaledOperator(operator, scalar)
       sop.direct(x) = scalar * operator.direct(x)
       sop.adjoint(x) = scalar * operator.adjoint(x)
       sop.norm() = operator.norm()
       sop.range_geometry() = operator.range_geometry()
       sop.domain_geometry() = operator.domain_geometry()
    '''
    def __init__(self, operator, scalar):
        if not isinstance (scalar, Number):
            raise TypeError('expected scalar: got {}'.format(type(scalar))
        self.scalar = scalar
        self.operator = operator
    def direct(self, x, out=None):
        return self.scalar * self.operator.direct(x, out=out)
    def adjoint(self, x, out=None):
        if self.operator.is_linear():
            return self.scalar * self.operator.adjoint(x, out=out)
    def size(self):
        return self.operator.size()
    def norm(self):
        return self.operator.norm()
    def range_geometry(self):
        return self.operator.range_geometry()
    def domain_geometry(self):
        return self.operator.domain_geometry()
        