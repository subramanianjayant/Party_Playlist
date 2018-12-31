import spotipy
import sys
import spotipy.util as util

def get_tracks(username):
	id_ = '481ac8972cbe40cca942de2fe72ceb57'
	secret_ = '6e4286b931b4408b98addea1d581ed35' 
	uri_ = 'http://localhost:3000/callback/'
	scope = 'user-top-read'
	token = util.prompt_for_user_token(username, scope, client_id=id_, client_secret=secret_,redirect_uri=uri_)
	
	if token:
		sp = spotipy.Spotify(auth=token)
		print sp.current_user()
		print '\n\n'
		results = sp.current_user_top_tracks(limit=25,time_range='short_term')
		print [str(track['name']) for track in results['items']]
		return set([track['id'] for track in results['items']])
	else:
		print "Unable to get auth token for %s" % username

if __name__ == '__main__':
	if len(sys.argv) > 1:
		user = sys.argv[1]
	else:
		print 'Usage: %s username' % (sys.argv[0])
		sys.exit()
	tracks = get_tracks(user)
