import unittest
from pathlib import Path
from tempfile import NamedTemporaryFile

from sentiment_analyzer import SentimentAnalyzer


class SentimentTrainingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analyzer = SentimentAnalyzer()

    def test_trains_from_good_and_bad_review_sections(self):
        reviews_path = Path(__file__).with_name("test_reviews.txt")

        review_count = self.analyzer.train_from_file(reviews_path)

        self.assertEqual(review_count, 6)
        positive = self.analyzer.analyze_sentiment_advanced(
            "The sound is elegant, silky, and great."
        )
        negative = self.analyzer.analyze_sentiment_advanced(
            "Do not buy these. The quality is disappointing."
        )
        self.assertEqual(positive["sentiment"], "Positive")
        self.assertEqual(negative["sentiment"], "Negative")

    def test_rejects_files_without_labeled_star_reviews(self):
        with NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as file:
            file.write("Good:\nThis is a good product.\n")
            file_path = Path(file.name)

        try:
            with self.assertRaisesRegex(ValueError, "No labeled reviews"):
                self.analyzer.train_from_file(file_path)
        finally:
            file_path.unlink()


if __name__ == "__main__":
    unittest.main()
