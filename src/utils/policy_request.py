""" a request object """


class PolicyRequest( object ):
    """ map policy request to object """

    def __init__(self, age: float, income: float, debt: float, remarks: int,
                 remarks_12m: int):
        self.age = age
        self.income = income
        self.debt = debt
        self.remarks = remarks
        self.remarks_12m = remarks_12m
