thondef clean_text(text):
"""
Utility function to clean and strip unwanted characters from the text.
"""
return text.strip().replace('\n', ' ').replace('\r', '')