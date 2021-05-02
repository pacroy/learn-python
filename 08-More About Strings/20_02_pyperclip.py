# Install with 'pip install pyperclip'
import pyperclip

print('Current clipboard: ' + pyperclip.paste())
pyperclip.copy('Hello!')
print(pyperclip.paste())
