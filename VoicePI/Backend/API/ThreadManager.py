import threading


class ThreadManager:
    AllThreads = []
    MusicThreads = []
    
    @staticmethod
    def completeAllThreads():
        ThreadManager.AllThreads = [].append(ThreadManager.MusicThreads)

    @staticmethod
    def AddThread(func, args, stopTh): # func -> function to run in Thread, args -> argument List, stopTh -> func to stop thread
        th = threading.Thread(target=func, args=args)
        ThreadManager.AllThreads.append((th, stopTh))
        th.start()

    @staticmethod
    def AddMusicThread(func, args, stopTh):
        th = threading.Thread(target=func, args=args)
        ThreadManager.MusicThreads.append((th, stopTh))
        th.start()

    @staticmethod
    def StopAllMusic():
        for thread in ThreadManager.MusicThreads:
            print("SUS:")
            thread[1]()