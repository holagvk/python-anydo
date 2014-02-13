# -*- coding: utf-8 -*-
#  Copyright 2011 Takeshi KOMIYA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  original source from: ('https://bitbucket.org/tk0miya/blockdiag'
#                         '/src/0789c102744c92767f0f0efb87b1b297741bb04c'
#                         '/src/blockdiag/tests/test_pep8.py')
#
from __future__ import print_function
import os
import sys
import pep8

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)


def test_pep8():
    arglist = [['statistics', True],
               ['show-source', True],
               ['repeat', True],
               ['paths', [BASE_DIR]]]

    pep8style = pep8.StyleGuide(arglist, parse_argv=False, config_file=True)
    options = pep8style.options
    if options.doctest:
        import doctest
        fail_d, done_d = doctest.testmod(report=False, verbose=options.verbose)
        fail_s, done_s = pep8.selftest(options)
        count_failed = fail_s + fail_d
        if not options.quiet:
            count_passed = done_d + done_s - count_failed
            print("%d passed and %d failed." % (count_passed, count_failed))
            if count_failed:
                print("Test failed.")
            else:
                print("Test passed.")
        if count_failed:
            sys.exit(1)
    if options.testsuite:
        pep8.init_tests(pep8style)
    report = pep8style.check_files()
    if options.statistics:
        report.print_statistics()
    if options.benchmark:
        report.print_benchmark()
    if options.testsuite and not options.quiet:
        report.print_results()
    if report.total_errors:
        if options.count:
            sys.stderr.write(str(report.total_errors) + '\n')
        #sys.exit(1)

    # reporting errors (additional summary)
    errors = report.get_count('E')
    warnings = report.get_count('W')
    message = 'pep8: %d errors / %d warnings' % (errors, warnings)
    print(message)
    assert report.total_errors == 0, message
