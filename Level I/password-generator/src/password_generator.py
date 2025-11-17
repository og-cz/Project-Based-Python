import random
import nltk
nltk.download('words')

def linear_random_generator(x0, a, b, m, n):
    results = []
    for _ in range(n):
        x0 = (a * x0 + b) % m
        results.append(x0)
    return results

class PasswordGenerator:
    type = ['random_password', 'memorable_password', 'pin']
    
    def __init__(self, type=type, choosed_type=0):
        try:
            self._choosed_type = choosed_type
            self._type = type[self._choosed_type]
        except Exception as e:
            print(e)
            
    def choose_type(self, **kwargs):
        match self._choosed_type:
            case 0:
                return RandomPasswordGenerator().generate(**kwargs)
            case 1:
                return MemorablePasswordGenerator().generate(**kwargs)
            case 2:
                return PinCodeGenerator().generate(**kwargs)

    def get_type(self):
        return self._type
    
class RandomPasswordGenerator:
    def generate(self, limit=None, choice=None):
        all_charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789"
        alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        charset = all_charset if choice else alphabets
        
        x0 = random.randint(2,70)
        a = random.randint(150_000,200_000)
        b = 1231
        m = len(charset)
        n = limit
        x = linear_random_generator(x0,a,b,m,n)
        result_string=''.join(charset[_] for _ in x)
        return f'Your generated password: {result_string}'

class MemorablePasswordGenerator:
    def generate(self, no_of_words=3, separator="-", capitalization=False):
        vocabulary = nltk.corpus.words.words()
        password_words = [random.choice(vocabulary) for _ in range(no_of_words)]
        if capitalization:
            password_words = [word.upper() for word in password_words]
        return separator.join(password_words)

class PinCodeGenerator:
    def generate(self, limit):
        charset = '0123456789'
        x0 = random.randint(2,70)
        a = random.randint(150_000,200_000)
        b = 1231
        m = len(charset)
        n = limit
        x = linear_random_generator(x0,a,b,m,n)
        result_string=''.join(charset[_] for _ in x)
        return f'Your new generated PIN: {result_string}'
    

