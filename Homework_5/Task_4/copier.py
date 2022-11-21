def copy_to_file(file_name, txt):
    file = open(file_name, 'w')
    file.write(txt)
    file.close()
