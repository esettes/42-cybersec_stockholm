import os

def main():

    folder = "infection"
    for count, filename in enumerate(os.listdir(folder)):
        rename = filename + '.ft'
        src = folder + '/' + filename
        dst = folder + '/' + rename
        print(filename, src)
        if not filename.endswith('.ft'):
            os.rename(src, dst)

if __name__ == '__main__':
    main()
