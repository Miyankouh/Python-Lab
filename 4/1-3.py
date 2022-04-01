# function description

def get_file_extension(file_name):
    "Beat-it.mp3"
    file_extension = file_name[len(file_name)-3:]
    return file_extension

# function call
print(get_file_extension("good-func.mp3"))
print(get_file_extension("good-func.xls"))
print(get_file_extension("good-func.img"))
print(get_file_extension("good-func.mp4"))