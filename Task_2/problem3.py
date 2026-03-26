sentence = input()

words = sentence.split()      
reversed_words = words[::-1] 
result = " ".join(reversed_words)  

print(result)