import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_positive_sentiment(self):
        result = sentiment_analyzer("I love this product, it's amazing!")
        self.assertEqual(result['label'], 'SENT_POSITIVE')

    def test_negative_sentiment(self):
        result = sentiment_analyzer("I hate everything about this experience.")
        self.assertEqual(result['label'], 'SENT_NEGATIVE')

    def test_neutral_sentiment(self):
        result = sentiment_analyzer("It is a table.")
        self.assertEqual(result['label'], 'SENT_NEUTRAL')

    def test_empty_input(self):
        result = sentiment_analyzer("")
        self.assertIsNone(result['label'])
        self.assertIsNone(result['score'])

if __name__ == '__main__':
    unittest.main()
