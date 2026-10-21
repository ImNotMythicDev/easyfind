import os

file = input("Path to file (Drag and drop works, depending on Terminal App):")
search = input("Search text you wanna find :")

os.system(f"cat {file} | grep {search}")
