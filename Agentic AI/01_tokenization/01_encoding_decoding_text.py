#tiktoken is a tokenizer from OpenAI to tokenize the text
import tiktoken

#Tokens - Tokens are pieces of text (like words, subwords, or characters) that a model processes. Each token is then mapped to a number (ID)
#Tokenization - Tokenization is the process of breaking text into smaller units (tokens). These tokens are then converted into numerical IDs.
#The model takes token IDs as input and predicts the probability of the next token. This process repeats step-by-step until a stopping condition (like an end token or max length).
#Then de-encode the tokens and return the text

text = "Hey, My name is Ashiq. My favorite sport is football. And my favorite footballer is Ricardo Kaka"
encode = tiktoken.encoding_for_model("gpt-4o") # This selects the tokenizer used by GPT-4o (not the model itself)
encoded_text = encode.encode(text)
print(f"Encoded {text}. The tokens are - {encoded_text}")
# The tokens are - [25216, 11, 3673, 1308, 382, 23582, 24366, 13, 3673, 8340, 9373, 382, 13332, 13, 1958, 922, 8340, 13332, 259, 382, 75127, 658, 3578]
print("="*30)
# Decoding - >
decoded_text = encode.decode([25216, 11, 3673, 1308, 382, 23582, 24366, 13, 3673, 8340, 9373, 382, 13332, 13, 1958, 922, 8340, 13332, 259, 382, 75127, 658, 3578])
print(f"Decoding {encoded_text}. The text is- {decoded_text}")