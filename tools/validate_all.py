from microformats2 import validate

import json
import sys
import os

success = 0
failure = 0

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        if f.endswith('.json'):
            fullpath = os.path.join(root, f)
            data = json.loads(open(fullpath, 'rb').read())
            try:
                validate(data)
            except:
                print('F: ', fullpath)
                failure += 1
            else:
                success += 1

print('Results')
print('   Successes: ', success)
print('    Failures: ', failure)
print('       Total: ', success + failure)
