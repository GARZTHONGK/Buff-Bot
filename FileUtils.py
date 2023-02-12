import os


def writefile(name, text):
    # writes data to file
    with open(name, 'w', encoding='utf-8') as f:
        f.write(text)


def readfile(name):
    # reads and returns file
    text = None
    with open(name, 'r', encoding='utf-8') as f:
        text = str(f.read())
    return text


def appendfile(name, text):
    # add text to end of file
    if os.path.exists(name):
        with open(name, 'a', encoding='utf-8') as f:
            f.write(text)
    else:
        with open(name, 'w', encoding='utf-8') as f:
            f.close()


def get_mid_str(s, start_str, stop_str):
    # Find the end of the left text
    start_pos = s.find(start_str)
    if start_pos == -1:
        return None
    start_pos += len(start_str)
    # Find the starting position of the text on the right
    stop_pos = s.find(stop_str, start_pos)
    if stop_pos == -1:
        return None

    # Take out the text in the middle by slicing
    return s[start_pos:stop_pos]
