from django.test import TestCase
from .models import Editor,Articles,tags
import datetime as dt



# Create your tests here.
class EditorTestClass(TestCase):
    #set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    def test_query(self):
        self.assertEquals(self.james.first_name,'James')
    def test_query2(self):
        self.assertEquals(self.james.last_name,'Muriuki')


    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    # def test_delete_method(self):
    #     self.james.delete_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors)>0)

    # def test_display_method(self):
    #     self.james.display_all()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors)>0)

class ArticlesTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_Articles= Articles(title = 'Test Articles',post = 'This is a random test Post',editor = self.james)
        self.new_Articles.save()

        self.new_Articles.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Articles.objects.all().delete()


    def test_get_news_today(self):
        today_news = Articles.todays_news()
        self.assertTrue(len(today_news)>0)


    