import os, shutil

def copy_files_ext(source, destination, files_type):
      for path, dirs, file_names in os.walk(source):
            for file_name in file_names:
                  if file_name.endswith(files_type):
                        file = os.path.join(path, file_name)
                        try:
                              shutil.copy(file, destination)
                        except FileExistsError:
                              continue

def main():
      # Settings

      # Files type
      files_type = '.pdf'

      # Source path
      source = "C:\\Data\\200305_Journal_Data"

      # Destination path
      destination = "C:\\Data\\200305_Journal_Data_PDFs"

      copy_files_ext(source, destination, files_type)

if __name__ == '__main__':
      main()

# %%
for index, path, dirs, file_names in os.walk(source):
      print(index)
      print(path)
      print(dirs)
      print(file_names)
      if index == 50:
            break