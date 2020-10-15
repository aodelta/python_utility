# Guillaume Vanleene 2020
# Script permetant de trier tout les nomds des fichiers dans un dossier en supprimant les charactères inutiles au début, à la fin, et en replacant l'index au début
# s'il y en a un

import pathlib
import sys

def rename_all_files_in_dir(dir, first_char = 0, latest_char = 0, _sorted = False):

   output = ['', []]
   error_occured = False

   if _sorted:
      for path in pathlib.Path(dir).iterdir():
         if path.is_file():

            file_name = path.name
            enum_index = 0
            file_index = ""

            try:
               enum_index = file_name.index("#")
            except ValueError:
               output[1].append(('HASGTAG NOT FOUND', file_name))
               error_occured = True
            else:
               enum_index += 1
               while(True) and enum_index <= len(file_name):
                  if file_name[enum_index].isdigit():
                     file_index += file_name[enum_index]
                     enum_index += 1
                  else:
                     break
            
               # Removing index
               file_name = file_name[:enum_index - len(file_index) - 2] + file_name[enum_index:]

               try:
                  file_index = int(file_index)
               except ValueError:
                  output[1] += ('ERROR GET INDEX', file_name)

               # Removing start & end
               file_name = file_name[first_char:len(file_name) - latest_char - len(path.suffix)] + file_name[len(file_name) - len(path.suffix):]

               new_name = "#{0} {1}".format(file_index, file_name)

               path.rename(pathlib.Path(path.parent, new_name))
   else:
      for path in pathlib.Path(dir).iterdir():
         if path.is_file():

            file_name = path.name

            directory = path.parent

            # Removing start & end
            file_name = file_name[first_char:len(file_name) - latest_char - len(path.suffix)] + file_name[len(file_name) - len(path.suffix):]

            new_name = "{0}".format(file_name)

            path.rename(pathlib.Path(directory, new_name))

   if error_occured:
      output[0] = 1
   else:
      output[0] = 0

   return output


directory = ""
latest_char = 0
first_char = 0
_sorted = False

# Dir
while(True):
   print("Directory : ")
   directory = input(" > ")
   if directory == "q" or directory.lower == "quit":
      sys.exit(0)
   if not pathlib.Path(directory).exists():
      print("Not a valid path")
   else:
      break

# FirstChar
while(True):
   print("How many char to remove at the begining : ")
   first_char = input(" > ")
   if first_char == "q" or first_char == "quit":
      sys.exit(0)
   if first_char == "":
      first_char = 0
      break
   try:
      first_char = int(first_char)
   except (ValueError, first_char < 0) as Exception:
      print("Not a valid number")
   else:
      break

# Latest Char
while(True):
   print("How many char to remove at the end : ")
   latest_char = input(" > ")
   if latest_char == "q" or latest_char == "quit":
      sys.exit(0)
   if latest_char == "":
      latest_char = 0
      break
   try:
      latest_char = int(latest_char)
   except (ValueError, latest_char < 0) as Exception:
      print("Not a valid number")
   else:
      break

# Enumerated ?
while(True):
   print("Are files enumerated (#x) and must be sorted ([y]es/[n]o)")

   answer = input(" > ")

   if answer == "q" or answer == "quit":
      sys.exit(0)
   if answer.lower() == "y" or answer.lower() == "yes":
      _sorted = True
      break
   elif answer.lower() == "n" or answer.lower() == "no":
      _sorted = False
      break
   else:
      print("Not a valid answer")

result = rename_all_files_in_dir(directory, first_char, latest_char, _sorted)

if result[0] == 0:
   print("\nL'opération à bien réussie")
if result[0] == 1:
   print("\nL'opération a rencontré certaines erreurs :")
   for error in result[1]:
      print("  - ", error[0], ":", error[1])