import re
from googlesearch import search


def get_anime_opening_given_string(string):
    modified_string = re.sub(r"(\((?:[^()\n]++|(?1))*\))(?=[^()\n]*$)", "", string)
    print(modified_string)


get_anime_opening_given_string(""""Hikaru nara (光るなら)" by Goose house (eps 1-11)'""")
