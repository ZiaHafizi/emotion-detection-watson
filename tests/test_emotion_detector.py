import unittest
from emotion_detector import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_mock_output(self):
        text = "I am happy"
        result = emotion_detector(text)
        self.assertIsInstance(result, dict)
        self.assertIn("joy", result)
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_empty_input(self):
        result = emotion_detector("")
        self.assertIsNone(result["anger"])
        self.assertIsNone(result["dominant_emotion"])

if __name__ == "__main__":
    unittest.main()
