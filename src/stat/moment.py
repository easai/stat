import math


class Moment:
    """ Calculate statistic moment
    """
    @staticmethod
    def moment(x, k):
        """ Calculate statistic moment

        Args:
            x(list): list of values
            k(int): degree

        Returns:
            kth moment of x
        """
        n = len(x)
        if n == 0:
            return None
        sum = 0
        for i in x:
            sum += i ** k
        return sum / n
