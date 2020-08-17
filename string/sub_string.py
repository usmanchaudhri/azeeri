


if __name__ == "__main__":
    # extract 'm' from the string
    text = "usman"
    idx = text.find('m')
    print(idx)
    print(text[0:idx] + text[idx+1:len(text)])
