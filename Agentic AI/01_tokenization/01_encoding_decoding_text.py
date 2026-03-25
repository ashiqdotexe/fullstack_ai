#tiktoken is a tokenizer from OpenAI to tokenize the text
import tiktoken

#Tokens - The mapped numbers those are converted from a text are called tokens
#Tokenization - Converting the text into a mapped or sequence of number is called tokenization
#We give the tokens to the transformer and it predicts the next tokens. This loop continues until it sees the end and return the sequence of tokens.
#Then de-encode the tokens and return the text

text = "Hey, My name is Ashiq. My favorite sport is football. And my favorite footballer is Ricardo Kaka"
encode = tiktoken.encoding_for_model("gpt-4o") # Choosing "gpt-4o" as encoding model, we can choose other as well
encoded_text = encode.encode(text)
print(f"Encoded {text}. The tokens are - {encoded_text}")
# The tokens are - [25216, 11, 3673, 1308, 382, 23582, 24366, 13, 3673, 8340, 9373, 382, 13332, 13, 1958, 922, 8340, 13332, 259, 382, 75127, 658, 3578]
print("="*30)
