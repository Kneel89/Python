#! python3
# backupToZip.py - Copies and entire folder
# and its contents into a ZIP file whoe filenme increments

import zipfile, os
def backupToZip(folder):
    os.chdir(folder)
    # Backup the entire contents of "folder" into a ZIP file
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on what exists
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Create the ZIP file.
    backupZip = zipfile.ZipFile(zipFilename,'w')
    
    # TODO: Walk the entire folder tree and compress the files in each folder.
    
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
    # Add the current folder to the ZIP file.
        backupZip.write(foldername)
    for filename in filenames:
        newBase = os.path.basename(folder) + '_'
        if filename.startswith(newBase) and filename.endswith('.zip'):
            continue # don't backup the backup ZIP files
        backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
                

    
backupToZip('C:\\Users\\Neil\\Documents\\Programming\\Python\\Backups\\Examples')
