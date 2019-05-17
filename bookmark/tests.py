from django.test import TestCase

from .models import Bookmark
from django.urls import reverse, NoReverseMatch


# Create your tests here.

def create_bookmark(site_name, url):
    return Bookmark.objects.create(site_name=site_name, url=url)


class BookmarkIndexViewTests(TestCase):

    # 목록이 없는경우(데이터가 없는경우)
    def test_no_bookmark(self):
        response = self.client.get(reverse('bookmark:list'))
        self.assertEqual(response.status_code, 200)  # a == b
        self.assertContains(response, "no bookmark list")
        self.assertQuerysetEqual(response.context['bookmark_list'], [])

    # 데이터 생성 했을경우
    def test_past_bookmark(self):
        create_bookmark(site_name='google', url='http://google.com')
        response = self.client.get(reverse('bookmark:list'))
        self.assertQuerysetEqual(response.context['bookmark_list'], ['<Bookmark: 이름 : google, 주소 : http://google.com>'])


class BookmarkDetailViewTests(TestCase):

    def test_no_detail(self):
        response = self.client.get(reverse('bookmark:detail', args=None))
        self.assertEqual(response, NoReverseMatch)

    def test_detail(self):
        bookmark = create_bookmark(site_name='google', url='http://google.com')
        url = reverse('bookmark:detail', args=(bookmark.id, ))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, bookmark.site_name)
        self.assertContains(response, bookmark.url)



