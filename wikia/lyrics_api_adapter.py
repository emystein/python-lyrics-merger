import lyricwikia


class WikiaLyricsAdapter(object):
    def get_lyrics(self, artist, title):
    	return lyricwikia.get_lyrics(artist, title)
