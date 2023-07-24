import os 
import shutil

#Path and source2 are the source directories 
#The rest are destinations paths to put the files in
path = "/mnt/c/Users/shezi/Downloads"
source2 = "/mnt/c/Users/shezi/Scripts"
imageDist = "/mnt/c/Users/shezi/OneDrive/Pictures/Downloaded"
musicDist = "/mnt/c/Users/shezi/Music"

#stores the paths as a list
dirs = os.listdir(path)
youtube_downloads = os.listdir(source2)

#lists of common extentions for images and audios
common_img = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".psd")
common_aud = (".mp3", ".wav", ".ogg", ".flac", ".aac", ".wma", ".m4a")

#Operating for each item in the list of paths
for entry in dirs :
    if entry:
        if entry.endswith(common_img):
            src_path = os.path.join(path, entry)
            dst_path = os.path.join(imageDist, entry)
            shutil.move(src_path, dst_path)
            
            #Prints the file being moved
            print("File '%s' has been move" % entry)
        
        elif entry.endswith(common_aud):
            src_path = os.path.join(path, entry)
            dst_path = os.path.join(musicDist, entry)
            shutil.move(src_path, dst_path) 
            
            #Prints the file being moved
            print("File '%s' has been move" % entry)
                 
unmoved = os.listdir(path)

#jpg is just an item could be replaced with i
#This is to check if there are files not moved
for jpg in unmoved:
    if jpg.endswith(common_img):
        print("Did not move '%s'" %jpg)
 
    elif jpg.endswith(common_aud):
        print("Did not move '%s'" %jpg)

    # else:
    #     print(jpg)

for auds in youtube_downloads:
    if auds.endswith(common_aud):
        src = os.path.join(source2, auds)
        dst = os.path.join(musicDist, auds)
        shutil.move(src, dst)
        
        #Prints the file being moved
        print("File '%s' has been move" % auds)
        