


class Keyword:
    ALL_Keywords = []

    def __init__(self, keyword, action, priority):
        self.keyword = keyword
        self.action = action
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    @staticmethod
    def findKeyword(msg):
        Keyword.ALL_Keywords.sort()
        print(Keyword.ALL_Keywords[0].priority)
        for elem in Keyword.ALL_Keywords:
            if elem in msg:
                elem.action(msg)
                return