class StringHelper:
    
    @staticmethod
    def reverse(text):
        new = ""
        for i in range(len(text)):
            new = text[i] + new  
        return new
    
    @staticmethod
    def count_letters(text):
        count = 0
        for char in text:
            count += 1
        return count

print(StringHelper.reverse("Привет")) 
print(StringHelper.count_letters("Привет")) 
