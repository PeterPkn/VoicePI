


class Keyword:
    ALL_Keywords = []

    def __init__(self, keyword, action, priority):
        self.keyword = keyword
        self.action = action
        self.priority = priority
        Keyword.ALL_Keywords.append(self)
    
    def __lt__(self, other):
        return self.priority < other.priority

    @staticmethod
    def findKeyword(msg):
        Keyword.ALL_Keywords.sort()
        for elem in Keyword.ALL_Keywords:
            if elem.keyword in msg:
                print("You said: " + elem.keyword)
                return elem.action(msg)
                