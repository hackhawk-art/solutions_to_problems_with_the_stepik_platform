import string

class CaesarCipher:
    def __init__(self, shift):
        self._shift = shift
        
    def encode(self, text):
        res = ""
        for i in text:
            if ord("a") <= ord(i) <= ord("z"):
                base = ord('a')
                alpha_index = ord(i) - base
                shifted_index = (alpha_index + self._shift) % 26
                res += chr(base + shifted_index)
            elif ord("A") <= ord(i) <= ord("Z"):
                base = ord('A')
                alpha_index = ord(i) - base
                shifted_index = (alpha_index + self._shift) % 26
                res += chr(base + shifted_index)
            else:
                res += i
        return res
    
    def decode(self, text):
        res = ""
        for i in text:
            if ord("a") <= ord(i) <= ord("z"):
                base = ord('a')
                alpha_index = ord(i) - base
                shifted_index = (alpha_index - self._shift) % 26
                res += chr(base + shifted_index)
            elif ord("A") <= ord(i) <= ord("Z"):
                base = ord('A')
                alpha_index = ord(i) + base
                shifted_index = (alpha_index - self._shift) % 26
                res += chr(base + shifted_index)
            else:
                res += i
        return res
    

# TEST_1:
cipher = CaesarCipher(10)

print(cipher.encode('Beegeek'))
print(cipher.decode('Gjjljjp'))

# TEST_2:
cipher = CaesarCipher(5)

print(cipher.encode('Биgeek123'))
print(cipher.decode('Биljjp123'))

# TEST_3:
cipher = CaesarCipher(10)

words = ['leader', 'life', 'central', 'whatever', 'true', 'show', 'year', 'teacher', 'happen', 'might', 'defense',
         'suggest', 'boy', 'trip', 'wish', 'interest', 'star', 'system', 'husband', 'wait', 'young', 'certainly',
         'with', 'wind', 'thought', 'hard', 'today', 'cup', 'where', 'fly', 'agreement', 'human', 'decision', 'along',
         'billion', 'prevent', 'authority', 'those', 'do', 'perform', 'plan', 'allow', 'president', 'do', 'around',
         'seven', 'dog', 'sea', 'use', 'my', 'head', 'whose', 'important', 'top', 'current', 'east', 'page', 'decide',
         'mouth', 'whatever', 'hospital', 'pattern', 'smile', 'probably', 'at', 'evening', 'current', 'local', 'want',
         'foreign', 'catch', 'option', 'meeting', 'course', 'collection', 'street', 'make', 'economic', 'fly', 'return',
         'experience', 'east', 'position', 'foot', 'one', 'mean', 'break', 'me', 'truth', 'management', 'want',
         'option', 'economic', 'response', 'attorney', 'table', 'push', 'travel', 'water', 'help']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_4:
cipher = CaesarCipher(15)

words = ['EvEr', 'WoUlD', 'CeRtAiN', 'WhIcH', 'WiTh', 'ThErE', 'EnViRoNmEnTaL', 'StRuCtUrE', 'NeWs', 'ThRoW', 'NoTe',
         'If', 'WiN', 'ShOuLdEr', 'NeEd', 'WhErE', 'MeThOd', 'FiRsT', 'CiViL', 'BaSe']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_5:
cipher = CaesarCipher(15)

words = ['civil😀', 'so😁', 'region☺', 'beat☺', 'artist😍', 'choice🙃', 'include🤭', 'degree😝', 'push🤪', 'side😏', 'size🤥',
         'policy🤨', '🤨🤥😏🤪😝🤭🙃😍☺😁😀']

encode_words = [cipher.encode(word) for word in words]
print(encode_words)

decode_words = [cipher.decode(word) for word in encode_words]
print(decode_words)

# TEST_6:
cipher = CaesarCipher(1)
print(cipher.encode('ZzzZzz'))
print(cipher.decode('AaaAaa'))