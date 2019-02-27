import unittest
from src.exercise_2.train import train_model
from sklearn.metrics import precision_score, recall_score


class TestModelMetrics(unittest.TestCase):
    def test_precision_should_be_above_0_point_8(self):
        text_clf, data_val, labels_val = train_model()

        y_pred = text_clf.predict(data_val)
        y_true = labels_val
        p = precision_score(y_true, y_pred)

        self.assertGreaterEqual(p, 0.5)

    def test_recall_should_be_above_0_point_8(self):
        text_clf, data_val, labels_val = train_model()

        y_pred = text_clf.predict(data_val)
        y_true = labels_val
        r = recall_score(y_true, y_pred)

        self.assertGreaterEqual(r, 0.5)
