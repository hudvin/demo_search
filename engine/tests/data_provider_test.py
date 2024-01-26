import json
import os
import tempfile
import unittest

from ..impl import DataProvider, OriginalDocument


class TestDataProvidder(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.sample_data = [
            {"text_content": "Text 1", "article_name": "Article 1", "link": "Link 1"},
            {"text_content": "Text 2", "article_name": "Article 2", "link": "Link 2"},
            {"text_content": "Text 3", "article_name": "Article 3", "link": "Link 3"}
        ]
        with open(self.temp_file.name, 'w', encoding='utf-8') as file:
            for data in self.sample_data:
                file.write(json.dumps(data) + '\n')

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_get_documents(self):
        data_provider = DataProvider(self.temp_file.name)
        documents = data_provider.get_documents()

        self.assertEqual(len(documents), len(self.sample_data))

        for i, document in enumerate(documents):
            self.assertIsInstance(document, OriginalDocument)
            self.assertEqual(document.text_content, self.sample_data[i]["text_content"])
            self.assertEqual(document.article_name, self.sample_data[i]["article_name"])
            self.assertEqual(document.link, self.sample_data[i]["link"])


if __name__ == '__main__':
    unittest.main()
