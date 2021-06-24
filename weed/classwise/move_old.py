import os

directory = "x"
mixed_files_dir = "/home/nithin/gitsync/kalupu/weed_data/weed/classwise/"+directory
new_files_dir = "/home/nithin/gitsync/kalupu/original/"+directory+"/original"
dest_dir = "/home/nithin/gitsync/kalupu/original/"+directory

new_files = os.listdir(new_files_dir)
for f in os.listdir(mixed_files_dir):
    if not f in new_files and not f[:-4]+".jpg" in new_files :
        print(f)
        os.rename(os.path.join(mixed_files_dir,f),os.path.join(dest_dir,f))
