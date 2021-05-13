def f1(p, r):
    return (2 * p * r) / (p + r) if p + r > 0 else 0


class Metric:
    def __init__(self, tp, pd, rd):
        self.true_p = tp
        self.prec_denom = pd
        self.rec_denom = rd
