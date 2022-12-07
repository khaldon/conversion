import os, glob


file_name = "{}/media/*.*".format(os.getcwd())


def delete_contain_media():
    files = glob.glob(file_name)
    # print(files)
    for f in files:
        try:
            os.unlink(f)
        except OSError as e:
            print(e)


if __name__ == "__main__":
    delete_contain_media()
