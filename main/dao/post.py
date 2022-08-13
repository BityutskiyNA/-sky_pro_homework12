class Post:

    def __init__(self,
                 pic,
                 content):
        self.pic = pic
        self.content = content

    def __repr__(self):
        return f"Post" \
               f"{self.pic}" \
               f"{self.content}" \
               f")"
