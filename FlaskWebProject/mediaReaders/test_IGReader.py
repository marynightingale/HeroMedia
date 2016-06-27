from unittest import TestCase
from IGReader import IGReader


class TestIGReader(TestCase):
    def setUp(self):
        self.igReader = IGReader()

    def test_getLatestPosts(self):
        self.assertTrue(self.igReader.getLatestPosts())

    def test_getLatestPosts_count_two(self):
        posts = self.igReader.getLatestPosts(count=2)
        self.assertEqual(len(posts), 2)

    def test_getLatestPosts_count_zero(self):
        try:
            self.igReader.getLatestPosts(count=0)
            self.fail()
        except ValueError:
            self.assertTrue(True)

    def test_getLatestPosts_return_type(self):
        posts = self.igReader.getLatestPosts()
        for media in posts:
            try:
                _ = media.caption.text
            except:
                self.fail("Could not get post caption")
