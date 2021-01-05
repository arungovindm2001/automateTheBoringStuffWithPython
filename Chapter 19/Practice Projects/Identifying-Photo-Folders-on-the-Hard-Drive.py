import os
from PIL import Image

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not(filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue # skip to next filename
        else:
            # Open image file using Pillow.
            try:
                image = Image.open(foldername+'/'+filename)
            except Exception as UnidentifiedImageError:
                print(foldername+'/'+filename+' cannot be identified')
                continue
            width,height = image.size
        
            # Check if width & height are larger than 500.
            if width >500 and height>500:
                # Image is large enough to be considered a photo.
                numPhotoFiles += 1
            else:
                # Image is too small to be a photo.
                numNonPhotoFiles += 1
    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > len(filenames)//2:
        print(foldername)
        
print('Scanned all files successfully')
