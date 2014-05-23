# -*- coding: utf-8 -*-
"""
  Copyright 2011 Takeshi KOMIYA

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  original source from: ('https://bitbucket.org/tk0miya/blockdiag'
                         '/src/0789c102744c92767f0f0efb87b1b297741bb04c'
                         '/src/blockdiag/tests/test_pep8.py')
"""
from __future__ import print_function
import unittest
import os
import sys
import pep8
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)


class Pep8Tests(unittest.TestCase):
    """ Unit test Pep8 """

    def test_pep8(self):
        """ runner """
        arglist = [['statistics', True],
                   ['show-source', True],
                   ['repeat', True],
                   ['paths', [BASE_DIR]]]

        pep8style = pep8.StyleGuide(arglist,
                                    parse_argv=False,
                                    config_file=True)
        options = pep8style.options
        report = pep8style.check_files()
        if options.statistics:
            report.print_statistics()

        # reporting errors (additional summary)
        errors = report.get_count('E')
        warnings = report.get_count('W')
        message = 'pep8: %d errors / %d warnings' % (errors, warnings)
        print(message)
        assert report.total_errors == 0, message
