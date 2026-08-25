def remove_fourth_character(word: str) -> str:
    newstring = list(word)
    newstring.pop(3)
    word = "".join(newstring)
    return word


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
