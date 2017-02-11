from final import getMood
import pickle
def get_mood(username_t,username_i):
        mapping={'sadness':'0,0,255','angry':'255,0,0','happy':'0,255,0','surprise':'139,69,19','neutral':'189,183,107','fear':'255,165,0'}
        #Sad: Blue, Angry: Red, Happy: Green, Surprise: Brown, Neutral:Yellow,Fear:Orange
        
        mood=getMood(username_i,username_t)
        value=mood[0][0]
        print value
        with open('colorfile', 'wb') as fp:
                pickle.dump(mapping[value], fp)
        return mood
        

        

