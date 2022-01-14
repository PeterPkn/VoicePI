import threading


class ThreadManager:
    def __init__(self):
        self.AllThreads = []
        self.MusicThreads = []

        pass

    def completeAllThreads(self):
        self.AllThreads = [].append(self.MusicThreads)

    def AddThread(self, func, args, stopTh): # func -> function to run in Thread, args -> argument List, stopTh -> func to stop thread
        th = threading.Thread(target=func, args=args)
        self.AllThreads.append((th, stopTh))
        th.start()

    def AddMusicThread(self, func, args, stopTh):
        th = threading.Thread(target=func, args=args)
        self.AllThreads.append((th, stopTh))
        th.start()

    def StopAllMusic(self):
        for thread in self.MusicThreads:
            thread[1]()