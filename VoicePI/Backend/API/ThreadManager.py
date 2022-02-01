import threading


class ThreadManager:
    AllThreads = []
    MusicThreads = []
    VideoThreads = []
    FaceTrackingThreads = []
    PorcupineThreads = []
    
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
    def AddPorcupineThread(func, args, stopTh):
        th = threading.Thread(target=func, args=args)
        ThreadManager.PorcupineThreads.append((th, stopTh))
        th.start()

    @staticmethod
    def StopAllMusic():
        for thread in ThreadManager.MusicThreads:
            print("SUS:")
            thread[1]()

    @staticmethod
    def AddVideoThread(func, args, stopTh):
        th = threading.Thread(target=func, args=args)
        ThreadManager.VideoThreads.append((th, stopTh))
        th.start()

    @staticmethod
    def StopAllPorcupine():
        for thread in ThreadManager.PorcupineThreads:
            print("SUS:")
            thread[1]()

    @staticmethod
    def StopAllVideos():
        for thread in ThreadManager.VideoThreads:
            print("SUS:")
            thread[1]()

