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
                RandomPasswordGenerator().generate(self, **kwargs)
            case 1:
                MemorablePasswordGenerator().generate()
            case 2:
                PinCodeGenerator().generate()

    def get_type(self):
        return self._type

class RandomPasswordGenerator:
    def generate(self):
        
        
        return

class MemorablePasswordGenerator:
    def generate(self):
        print("Generating memorable password...")

class PinCodeGenerator:
    def generate(self):
        print("Generating pin code...")