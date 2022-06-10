import re


def main():
    file = open("access.txt", "r")
    lines = file.readlines()
    pattern = re.compile(r"GET /images/stands/TH_photo_[0-9]+\\.jpg HTTP/1\\.1\" 200")

    count = 0
    for line in lines:
        count += 1
        matches = pattern.match(line)
    print(count)


if __name__ == '__main__':
    main()
