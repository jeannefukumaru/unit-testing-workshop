import json 


def load_reviews(filepath):
    with open(filepath) as f:
        reviews = f.read().strip().split('\n')
        reviews = [json.loads(review) for review in reviews]
    return reviews

def get_binary_labels(reviews):
    return [0 if review['stars'] <= 3 else 1 for review in reviews]

def extract_texts_and_labels(reviews):
    texts  = [review['text'] for review in reviews]
    labels = get_binary_labels(reviews)

    return texts, labels