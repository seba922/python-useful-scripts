import re

def findExactLines():
    try:
        pattern = re.compile(r"^\d{4}-\d{2}-\d{2}")

        with open(r"data.log", 'r', encoding='utf-8') as dataFile, \
            open(f"result.log", 'w', encoding='utf-8') as outputFile:
            for index, line in enumerate(dataFile):
                done = False
                if pattern.match(line):
                    outputFile.write(f'index {index} {line}')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    findExactLines()