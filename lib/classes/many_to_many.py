class Article:   
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        '''get article title'''
        return self._title
    @title.setter
    def title(self, article_title):
        '''set article title'''
        if not isinstance(article_title, str) or len(article_title) > 50 or len(article_title) < 5 or hasattr(self, 'title'):
            raise Exception("Not a valid article title")
        else:
            self._title = article_title

    @property
    def author(self):
        '''get author'''
        return self._author
    @author.setter
    def author(self, article_author):
        '''set article author'''
        if not isinstance(article_author, Author):
            raise Exception("The article author must be an instance of Author.")
        else:
            self._author = article_author
    
    @property
    def magazine(self):
        '''get magazine'''
        return self._magazine
    @magazine.setter
    def magazine(self, article_magazine):
        '''set article magazine'''
        if not isinstance(article_magazine, Magazine):
            raise Exception("The article magazine must be an instance of Magazine")
        else:
            self._magazine = article_magazine
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        '''get name'''
        return self._name
    @name.setter
    def name(self, author_name):
        '''set name'''
        if hasattr(self, "name"):
            raise Exception("Cannot change author name")
        elif not isinstance(author_name, str):
            raise Exception(f"{author_name} isn't a string")
        elif len(author_name) < 1:
            raise Exception(f"{author_name} cannot be an empty string")
        else:
            self._name = author_name

    def articles(self):
        return [article for article in Article.all if article.author == self]
        # for article in Article.all:
        # if article.author == self:
        # print(article.magazine.category)

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.magazines()) < 1:
            return None
        else:
            return list(set([mag.category for mag in self.magazines()]))

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        '''get name'''
        return self._name
    @name.setter
    def name(self, magazine_name):
        '''set magazine name'''
        if not isinstance(magazine_name, str): 
            raise Exception("Magazine name should be a string")
        elif len(magazine_name) > 16 or len(magazine_name) < 2:
            raise Exception("Magazine name should be between 2 and 16 chars")
        else:
            self._name = magazine_name

    @property
    def category(self):
        '''get category'''
        return self._category
    @category.setter
    def category(self, magazine_category):
        '''set category'''
        if not isinstance(magazine_category, str) or magazine_category == "":
            raise Exception("Not Valid")
        else:
            self._category = magazine_category

    def articles(self):
        return [art for art in Article.all if art.magazine == self]
        # for art in Article.all:
        # print(art.magazine.name)

    def contributors(self):
        return list(set([art.author for art in self.articles()]))

    def article_titles(self):
        if len(self.articles()) < 1:
            return None
        else:
            return [article.title for article in self.articles()]
     

    def contributing_authors(self):
        counting_authors = {}
        for article in self.articles():
            if article.author in counting_authors:
                counting_authors[article.author] += 1
            else:
                counting_authors[article.author] = 1
        contributing_auth = []
        for author, count in counting_authors.items():
            if count > 2:
                contributing_auth.append(author)
        if not contributing_auth:
            return None
        else:
            return contributing_auth
    @classmethod
    def top_publisher(cls):
        '''get top publisher'''
        if not Article.all:
            return None
        else:
            counting_magazine_articles = {}
            for article in Article.all:
                if article.magazine in counting_magazine_articles:
                    counting_magazine_articles[article.magazine] += 1
                else:
                    counting_magazine_articles[article.magazine] = 1
            
            best_magazine_publisher = None
            max_count = 0
            for magazine, count in counting_magazine_articles.items():
                if count > max_count:
                    max_count = count
                    best_magazine_publisher = magazine
            return best_magazine_publisher