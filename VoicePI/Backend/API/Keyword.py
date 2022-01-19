


class Keyword:
    ALL_Keywords = []

    @staticmethod
    def createKeywords():
        
        def play_action(a_string):
            music = MusicPlayer(a_string)
            music.start()
            infos = music.getMetadata()
            speak(f'Started playing: {infos[0]} from {infos[1]}')
            return jsonify({'answ':f'Started playing: {infos[0]} from {infos[1]}'})

        def listenbg_action(a_string):
            if 'listen bg stop' in a_string:
                try:
                    stop_listening()
                    return jsonify({'answ':f'Stopped Listening in the Background'})
                except error:
                    print('Could not stop Background Listening!')
                    
            stop_listening = listen_in_bg()
            return jsonify({'answ':f'Listening in the Background'})

        def stop_action(a_string):
            ThreadManager.StopAllMusic()
            ThreadManager.StopAllVideos()
            speak('Stopping all Music and Videos.')
            return jsonify({'answ':'Stopping all Music.'})

        def speak_action(a_string):
            speak(a_string[5:])
            return {'answ':a_string[5:]}

        def listen_action(a_string):
            req = listen()
            print(req['query'])
                
            if 'play' in req or 'spiele' in req['query']:
                music = MusicPlayer(req['query'].replace('play','').replace('spiele', ''))
                infos = music.getMetadata()
                speak(f'Started playing: {infos[0]} from {infos[1]}')
                music.start()
                    
                return jsonify({'answ':f'Started playing: {infos[0]} from {infos[1]}'})

            elif 'show' in req or 'zeige' in req['query']:
                video = VideoPlayer(req['query'].replace('play','').replace('spiele', ''))
                infos = video.getMetadata()
                speak(f'Started playing: {infos[0]} from {infos[1]}')
                video.start()

        def show_action(a_string):
            video = VideoPlayer(a_string.replace('play','').replace('spiele', ''))
            infos = video.getMetadata()
            speak(f'Started playing: {infos[0]} from {infos[1]}')
            video.start()

        def sussy_action(a_string):
            speak('You sussy baka!')
            return jsonify({'answ':'You sussy baka.'})

        Keyword('play',play_action,1 )
        Keyword('spiele',play_action,1 )
        Keyword('listen bg',listenbg_action,2 )
        Keyword('stop',stop_action,3 )
        Keyword('speak',speak_action,4 )
        Keyword('listen',listen_action,5 )
        Keyword('show',show_action,6 )
        Keyword('zeige',show_action,6 )


        Keyword('sus',sussy_action,100 )
        Keyword('among us',sussy_action,100 )
        Keyword('amogus',sussy_action,100 )
        Keyword('sussy',sussy_action,100 )

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
            if elem.keyword in msg.lower():
                print("You said: " + elem.keyword)
                return elem.action(msg)
        return {'answ':'No Action found!'}
                