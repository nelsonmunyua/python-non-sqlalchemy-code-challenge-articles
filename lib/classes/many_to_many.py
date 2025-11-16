class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be 5–50 chars")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title  # immutable

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name  # immutable

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = {article.magazine for article in self.articles()}
        return list(mags)

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        categories = {article.magazine.category for article in self.articles()}
        return list(categories)


class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = {article.author for article in self.articles()}
        return list(authors)

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """
        Return authors who wrote **2 or more** articles in this magazine
        """
        counts = {}
        for article in self.articles():
            counts[article.author] = counts.get(article.author, 0) + 1

        # 2 or more articles
        result = [author for author, count in counts.items() if count >= 2]

        return result if result else None
