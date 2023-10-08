import base64

MESSAGE = '''
H0YBHBYQSx4WVVRTTkMGAAwUBwlBRVUXBgIIBBMOABYJTV9SUwwdEAQXBBAXCUFFVREPCAsTBhpS
UxRNQhsaChwBBRsLGRYJQUVVFQoGDQQEDBgWQBlCUk5JSREPHgYWGEsJQl5UThwFAxAAAQAJTV9S
UxoPAgRVRVVUSAIKVVRTTkMWGwdUVFM=
'''

KEY = 'darius.mertin'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print(''.join(result))

# Message:
# {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}