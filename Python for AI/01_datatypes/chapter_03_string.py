# Indexing and slicing
description = "Bold and Aromatic"
print(f"The first word of description is {description[:4]} and the last word of description is {description[9:]}")
print(f"The reverse of description is {description[::-1]}")

#Encoding string-
label_text = "আমার সোনার বাংলা আমি তোমায় ভালোবাসি" 
encoded_text = label_text.encode("utf-8")
print(f"Label text is {label_text}")
print(f"Encoded text is {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text is {decoded_text}")