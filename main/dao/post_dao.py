import json
from exceptions.exceptions import DataSourceError
from main.dao.post import Post


class PostDAO:
    def __init__(self, path):
        self.path = path


    def _loadf(self):
        """

        """
        try:
            file = open(self.path, encoding="utf-8")
            post = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
             raise DataSourceError()

        list_of_posts = [Post(**posts_data) for posts_data in post]
        return list_of_posts


    def get_searcg(self, substring):
        """

        """
        substring = str(substring).upper()
        posts = self._loadf()
        found_posts = [post for post in posts if substring in post.content.upper()]

        return found_posts

    def add_post(self,pic ,content):
        """

        """
        posts = self._loadf()
        posts.append(Post(pic, content))

        # data = {'pic': pic ,'content':content}
        data = []
        for post in posts:
            data.append( {'pic': post.pic,'content': post.content})

        file = open(self.path, "w", encoding="utf-8")
        json.dump(data, file)
        file.close()

        return ""

# аfasfa = PostDAO("D:\python_pr\Sky_Pro_HW_12\data\posts.json")
# print(аfasfa)
# аfasfa.add_post("/uploads/images/cat.png","fasfsdfasfsadfasfsaf")

