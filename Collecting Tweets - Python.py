from __future__ import absolute_import, print_function
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler




c_k="D9K9CXZbZKRZqYXT7YhJ5Yx5q"

c_s="e24PT6VP96xjG1th2FSK5oyuMbnvwLPppFIw0tpeZWysFgeDLE"

a_t="4871769920-81XQGwUuZPfrgMxKCaCNNwhaHGzTVblEVyMGLFj"

a_t_s="96IeeRnuUZ3gXGURTgyEJFJX5SA1GNu1gtNDkGUFmkSvJ"

class Collector(StreamListener):
    
    def on_data(self, info):
        
		print(info)
		newFile = open('twittertweet.txt','a')
		newFile.write(info)
		newFile.write('\n')
		newFile.close()  
       		return True
	

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    x = Collector()
    auth = OAuthHandler(c_k, c_s)
    auth.set_access_token(a_t, a_t_s)

    stream = Stream(auth, x)
    stream.filter(track=['election','politics','politicians','vote','clinton','trump','republicans','democrats','sanders','cruz','kasich'])