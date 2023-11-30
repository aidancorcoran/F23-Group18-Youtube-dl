# coding: utf-8

from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from youtube_dl.options import parseOpts


class TestOptionsPlaylistTitle(unittest.TestCase):
    def test_option_sets_others(self):
        feature = "python ../youtube_dl/__main__.py --output-name-playlist https://www.youtube.com/watch?v=mKSNQuQrsm0&list=PL_ym6QHjS1swgJe7QmMQXwoZuMY7Tq0qT"
        old = "python ../youtube_dl/__main__.py --flat-playlist --dump-json --dump-single-json https://www.youtube.com/watch?v=mKSNQuQrsm0&list=PL_ym6QHjS1swgJe7QmMQXwoZuMY7Tq0qT"

        new_feature_parser, new_feature_opts, new_feature_args = parseOpts(feature)
        old_parser, old_opts, old_args = parseOpts(old)

        if(new_feature_opts == old_opts):
            print("Options match")


if __name__ == '__main__':
    unittest.main()
