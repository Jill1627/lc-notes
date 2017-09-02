"""
LC 535 Encode and decode tinyurl
Multiple ways to encode and decode tinyUrl
Idea: use a hashmap to <identifier : store long url>
"""
class Codec:
    def __init__(self):
        self.hm = dict()
        self.tinyUrlConst = "http://tinyurl.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        hashcode = id(longUrl)
        self.hm[hashcode] = longUrl
        return "http://tinyurl.com/" + str(hashcode)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.hm[int(shortUrl[len(self.tinyUrlConst) : ])]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
