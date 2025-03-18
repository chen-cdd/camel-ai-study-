import random

class NovelRecommendationTool:
    def __init__(self):
        # 示例小说数据，可以根据实际需求扩展
        self.novels = [
            {'title': 'The Great Gatsby', 'genre': 'Fiction', 'author': 'F. Scott Fitzgerald'},
            {'title': '1984', 'genre': 'Dystopian', 'author': 'George Orwell'},
            {'title': 'To Kill a Mockingbird', 'genre': 'Fiction', 'author': 'Harper Lee'},
            {'title': 'The Catcher in the Rye', 'genre': 'Fiction', 'author': 'J.D. Salinger'},
            {'title': 'Brave New World', 'genre': 'Dystopian', 'author': 'Aldous Huxley'},
            {'title': 'Moby Dick', 'genre': 'Adventure', 'author': 'Herman Melville'},
            {'title': 'Pride and Prejudice', 'genre': 'Romance', 'author': 'Jane Austen'},
            {'title': 'The Hobbit', 'genre': 'Fantasy', 'author': 'J.R.R. Tolkien'}
        ]
    
    def recommend_novel(self, genre=None, author=None):
        # 根据用户提供的参数推荐小说
        recommended = self.novels
        if genre:
            recommended = [novel for novel in recommended if genre.lower() in novel['genre'].lower()]
        if author:
            recommended = [novel for novel in recommended if author.lower() in novel['author'].lower()]
        
        # 如果没有推荐结果，则随机返回一部小说
        if not recommended:
            return random.choice(self.novels)
        
        return random.choice(recommended)

