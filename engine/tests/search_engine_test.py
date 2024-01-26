import unittest

from ..impl import SearchEngine, OriginalDocument


class TestSearchEngine(unittest.TestCase):

    def setUp(self):
        # Create some sample documents for testing
        self.documents = [
            OriginalDocument(
                text_content="In 1946, American theoretical astrophysicist Lyman Spitzer proposed to put a telescope in space.",
                article_name="Article 1", link="Link 1"),
            OriginalDocument(
                text_content="The first operational space telescopes were the American Orbiting Astronomical"
                             " Observatory, OAO-2 launched in 1968, and the Soviet Orion 1 ultraviolet telescope aboard space station Salyut 1 in 1971.",
                article_name="Article 2", link="Link 2"),
            OriginalDocument(
                text_content="Space telescopes are much more expensive to build than ground-based telescopes."
                             " Due to their location, space telescopes are also extremely difficult to maintain. ",
                article_name="Article 3", link="Link 3"),
            OriginalDocument(
                text_content="Balloon-borne telescopes have been used for observation from the stratosphere since the Stratoscope I was launched in 1957",
                article_name="Article 4", link="Link 4"),
            OriginalDocument(
                text_content="When fully inflated, the 40-million-cubic-feet helium balloon will be about 400 feet (150 meters) wide. "
                             "The current best estimate for the weight of the observatory, "
                             "including the gondola, solar panels, antenna, scientific instrument and communication systems, is about 5,500 pounds"
                             " (2,500 kilograms).",
                article_name="Article 5", link="Link 5")
        ]

        self.search_engine = SearchEngine(self.documents)

    def test_search(self):
        query = "Text"
        search_results = self.search_engine.search(query)

        self.assertIsNot(search_results, None)


if __name__ == '__main__':
    unittest.main()
