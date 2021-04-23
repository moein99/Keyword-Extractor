def precision(extracted_keywords, dataset_keywords):
    tp = len(set(extracted_keywords).intersection(set(dataset_keywords)))
    fp = len(extracted_keywords) - tp
    return tp / (tp + fp) if tp + fp > 0 else 0


def recall(extracted_keywords, dataset_keywords):
    tp = len(set(extracted_keywords).intersection(set(dataset_keywords)))
    fn = len(dataset_keywords) - tp
    return tp / (tp + fn) if tp + fn > 0 else 0


def f1(p, r):
    return (2 * p * r) / (p + r) if p + r > 0 else 0


class Metric:
    def __init__(self, p, r, f1):
        self.p = p
        self.r = r
        self.f1 = f1
