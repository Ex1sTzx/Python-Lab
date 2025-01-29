def string_functions():
    string = "  Hello, World!  "
    
    # Remove leading and trailing whitespaces
    stripped_string = string.strip()
    print("Stripped string:", stripped_string)
    
    # Remove leading whitespaces
    lstripped_string = string.lstrip()
    print("Lstripped string:", lstripped_string)
    
    # Remove trailing whitespaces
    rstripped_string = string.rstrip()
    print("Rstripped string:", rstripped_string)
    
    # Replace a substring
    replaced_string = string.replace("World", "Universe")
    print("Replaced string:", replaced_string)
    
    # Convert to lowercase
    lowercase_string = string.lower()
    print("Lowercase string:", lowercase_string)
    
    # Split the string into a list of words
    words = string.split()
    print("Words:", words)

string_functions()