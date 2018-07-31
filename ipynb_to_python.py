import json
import sys

# Usage syntax - python ipynb_to_python.py source.ipynb dest.py

def main(source, dest):
    file = open(source, 'r')
    json_text = json.load(file)
    file.close()

    cells = json_text['cells']
    py_file = open(dest,'w')
    for cell in cells:
        try:
            for line in cell['source']:
                py_file.write(line.strip('\n') + "\n")
        except:
            pass
        py_file.write("\n")
    py_file.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    exit(0)    