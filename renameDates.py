#! python3

#renameDates.py - Renames filenmes with American MM-DD-YYYY

import shutil, re, os

os.chdir('C:\\Users\\Neil\\Documents\\Programming\\Python\\American to European Dates')
datePattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$
""", re.VERBOSE)

# TODO: Loop over the files in the working directory.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
# TODO: Skip files without a date.
    if mo == None:
        continue

# TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

# TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
# TODO: Get the full, absolute file paths.
    absWorkDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkDir, amerFilename)
    euroFilename = os.path.join(absWorkDir, euroFilename)
        
# TODO: Rename the files.
    #print('Renaming "%s" to "%s"...' %(amerFilename, euroFilename))
    shutil.move(amerFilename,euroFilename)

