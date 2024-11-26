# This is code anonymise the sub domains of ip addresses
# Author: Andrew Beatty

import re

regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # we make a group at the
# beginning to keep
replacementText="\\1XXX.XXX " # note the space at the end to match above
filename = "programming_for_data_analytics/my_work/smaller_access.log"
outputFileName = "programming_for_data_analytics/my_work/anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            # for debugging
            #foundText = re.search(regex, line).group()
            #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            outputFile.write(newLine)