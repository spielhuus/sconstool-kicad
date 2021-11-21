#!/usr/bin/env python
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import json
from junit_xml import TestSuite, TestCase

##Build the junit report for jenkins
def convert(input, output) :
    test_suites = {}
    with open(input,) as f :
        data = json.load(f)
        for key, value in data.items():
            test_cases = []
            for key2, value2 in value.items():
                if( key2 == 'callouts' or key2 == 'summary' ) :
                    continue
                elif( key2 == 'unit_test' ) :
                    for item in value2['report']['tests'] :
                        test_case = TestCase('TEST', item['name'], (int)(item['duration']), item['outcome'], 'I am stderr!')
                        if item['outcome'] == "failed" :
                            test_case.add_failure_info( item['call']['longrepr'])
                        test_cases.append( test_case )

                else : 
                    for key3, value3 in value2.items():
                        if( key3 == 'bom' ) :
                            continue
                        elif( key3 == 'erc' ) :
                            for item in value3 :
                                out = ''
                                for con in item['con'] :
                                    out += con['x'] + '-' + con['y'] + ": " + con['message'] + "\n"
                                testname = key + "::" + key2 + "::" + item['sheet']
                                test_case = TestCase(testname, key3, (int)(item['code']), item['message'], "ERC")
                                test_case.add_failure_info( 'ERC Error' )
                                test_cases.append( test_case )

                        elif( key3 == 'drc' ) :
                            for item in value3 :
                                out = ''
                                for con in item['con'] :
                                    out += con['x'] + '-' + con['y'] + ": " + con['message'] + "\n"
                                testname = key + "::" + key2 + "::" + item['sheet']
                                test_case = TestCase(testname, key3, (int)(item['code']), item['message'], "DRC")
                                test_case.add_failure_info( 'DRC Error' )
                                test_cases.append( test_case )
                            
                        elif( key3 == 'unconnected' ) :
                            for item in value3 :
                                out = ''
                                for con in item['con'] :
                                    out += con['x'] + '-' + con['y'] + ": " + con['message'] + "\n"
                                testname = key + "::" + key2 + "::" + item['sheet']
                                test_case = TestCase(testname, key3, (int)(item['code']), item['message'], "unconnected")
                                test_case.add_failure_info( out )
                                test_cases.append( test_case )


            if test_cases :
                if key in test_suites :
                    test_suites[key].extend( test_cases )
                else :
                    test_suites[key] = test_cases
                        

    with open(output, 'w') as f:
        cases = []
        for case in test_suites :
            cases.append(TestSuite(case, test_suites[case]))
        TestSuite.to_file(f, cases, prettyprint=True)

