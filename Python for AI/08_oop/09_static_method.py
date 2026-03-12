# We use static method decorator so that we dont need to create any object
class Tea:
    @staticmethod
    def prepare(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , rice   , sugar  , tea"
cleaned_data = Tea.prepare(raw)
print(cleaned_data)