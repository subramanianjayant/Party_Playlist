import spotipy
import sys
import spotipy.util as util

def get_tracks(user):
	scope = 'user-top-read'
	token = util.prompt_for_user_token(user, scope, client_id=' 481ac8972cbe40cca942de2fe72ceb57', client_secret='6e4286b931b4408b98addea1d581ed35')
	
	if token:
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_top_tracks(limit=25,time_range='short_term')
	else:
		print "Unable to get auth token for %s" % user

def generate_playlist(users)

