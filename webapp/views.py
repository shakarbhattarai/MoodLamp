from django.shortcuts import render
from mood_to_color import get_mood      
from read_data import getData,getColor
from django.http import HttpResponse 
def index(request):
        
	
        if(request.method == 'GET'):
		instagramUsername = request.GET.get('instagramUsername')
		twitterUsername = request.GET.get('twitterUsername')
		images=[]
		if (instagramUsername != None and twitterUsername != None):
		        mood=get_mood(twitterUsername,instagramUsername)
		        print mood, "from views"
		        array,tweets,picture=getData()
		        for j in range(len(array)):
		                images.append(array[j])
		                
		        return render(request, 'webapp/index.html', {'tweets': tweets,'instaFeeds': images,'moods':mood,'picture':picture})
		else:
		        return render(request, 'webapp/index.html', {'tweets': ['Test Tweet 1','Test Tweet 1','Test Tweet 1'],'instaFeeds': ['Insta Feed 1','Insta Feed 2']})
def color(request):
           a=getColor()
           return HttpResponse(str(a))
	       
	
	        



