import unittest
from html.parser import HTMLParser
from pathlib import Path


class IndexParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.anchors = []
        self.iframes = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a":
            self.anchors.append(attrs_dict)
        elif tag == "iframe":
            self.iframes.append(attrs_dict)


class IndexHtmlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index_path = Path("index.html")
        cls.content = cls.index_path.read_text(encoding="utf-8")
        cls.parser = IndexParser()
        cls.parser.feed(cls.content)

    def test_has_four_channel_links(self):
        self.assertEqual(len(self.parser.anchors), 4)

    def test_channel_links_keep_security_attributes(self):
        for anchor in self.parser.anchors:
            self.assertEqual(anchor.get("target"), "_blank")
            rel = set(anchor.get("rel", "").split())
            self.assertTrue({"noopener", "noreferrer"}.issubset(rel))

    def test_has_twelve_embedded_videos(self):
        self.assertEqual(len(self.parser.iframes), 12)

    def test_embeds_use_youtube_embed_urls(self):
        for iframe in self.parser.iframes:
            src = iframe.get("src", "")
            self.assertIn("https://www.youtube.com/embed/", src)


if __name__ == "__main__":
    unittest.main()
