# ASCII Use Cases and Examples

# 1. Early Computing and Data Formats
# ASCII for text files and basic programming strings
text = "Hello, ASCII World!"  # ASCII string

# 2. Control Characters
# ASCII control characters for device control
newline = '\n'  # Line Feed (LF) ASCII control character

# 3. Networking and Communication
# ASCII in older network protocols like Telnet and FTP
command = 'GET'  # ASCII command for HTTP protocol

# Example: ASCII Art
ascii_art = """
  /\_/\\
 ( o.o )
  > ^ <
"""  # Simple ASCII art of a cat

# Print ASCII art
print(ascii_art)

# Unicode Use Cases and Examples

# 1. Globalization of Software and Websites
# Unicode for multilingual websites and software
multilingual_text = "こんにちは世界😊"  # Japanese and an emoji
'''
Breakdown of the String:
こんにちは (Konnichiwa): This is a common Japanese greeting 
that translates to "Hello" or "Good afternoon" in English.
世界 (Sekai): This is the Japanese word for "World".
😊: This is a Unicode character representing a smiling face emoji.
When combined, こんにちは世界😊 can be translated to 
"Hello, World 😊" in English, where the emoji adds a 
friendly and cheerful touch to the greeting.
'''

# 2. Database and File Storage
# Storing names and addresses in multiple languages in databases
# A Chinese phrase in Unicode
chinese_phrase = "美丽的世界"  # Means "Beautiful World" in English

# Print the Chinese phrase
print(chinese_phrase)


# 3. Programming Language Support
# Unicode in modern programming languages for internationalization
greeting = "Hola, Mundo!"  # Spanish greeting

# 4. Emojis and Special Characters
# Unicode for emojis and special symbols
emoji = "😊"  # Smiley face emoji
math_symbol = "∑"  # Summation symbol in Unicode

# Print Unicode examples
print(multilingual_text)
print(chinese_phrase)
print(greeting)
print(emoji)
print(math_symbol)

# Using Unicode directly
# Smiling face emoji using its Unicode code point
smiling_face_unicode = "\U0001F60A"
print(smiling_face_unicode)  # Output: 😊

# Copy and Paste method
# Directly copy and pasting the emoji into the code
smiling_face_copy_paste = "😊"
print(smiling_face_copy_paste)  # Output: 😊

# Using an emoji library
# First, you need to install the emoji library:
# pip install emoji

# import emoji

# # Using the emoji library to convert an alias to the actual emoji
# smiling_face_emoji_lib = emoji.emojize(':smile:')
# print(smiling_face_emoji_lib)  # Output: 😊


# Note: The above method requires the emoji library to be installed.
# It provides a more human-readable way to include emojis and a larger selection of emojis.
