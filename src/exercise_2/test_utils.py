import unittest
from exercise_2.utils import load_reviews, get_binary_labels, extract_texts_and_labels

class TestUtils(unittest.TestCase):
    def test_load_reviews(self):
        reviews = load_reviews('./data/review_100_samples.json')

        self.assertEqual(len(reviews), 100)
        self.assertEqual(type(reviews[0]), dict)
    
    def test_get_binary_labels_should_return_a_list_of_0s_and_1s(self):
        reviews = [ {'stars': 0}, 
                    {'stars': 2}, 
                    {'stars': 3}, 
                    {'stars': 4}]
        self.assertEqual([0, 0, 0, 1], get_binary_labels(reviews))

    def test_get_texts_and_labels_from_reviews(self):
        reviews = [{'text': 'this is great',
                    'stars': 4},
                   {'text': 'this is crap',
                    'stars': 1}]

        texts, labels = extract_texts_and_labels(reviews)

        self.assertEqual(['this is great', 'this is crap'], texts)
        self.assertEqual([1, 0], labels)
        