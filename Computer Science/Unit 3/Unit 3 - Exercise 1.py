progname = "Aenean eget vulputate nisl. Pellentesque at aliquam nunc, non condimentum."
print(progname)
spaces = 0
for x in range(len(progname)):
  program = progname[x]
  if program == " ":
    spaces += 1
print("There are", spaces, "spaces in the text.")
