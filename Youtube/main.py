import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'Replace with yours'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(q=options.q, part='id,snippet', maxResults=options.max_results).execute()

    videos = []
    channels = []
    playlists = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['snippet']['title']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append('%s' % (search_result['snippet']['title']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append('%s' % (search_result['snippet']['title']))

    print("{:>30}".format("Videos"), '\n',  "--"*45)
    print('\n'.join(videos), '\n')
    print("{:>30}".format("Channels"), '\n',  "--"*45)
    print ('\n'.join(channels), '\n')
    print("{:>30}".format("Playlists"), '\n',  "--"*45)
    print ('\n'.join(playlists), '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='item search')
    parser.add_argument('--max-results', help='Max results', default=number of results)
    args = parser.parse_args()

try:
    youtube_search(args)
except HttpError:
    print ("Error")
