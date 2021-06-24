import os
label_dir = "../../labels/train"

for f in os.listdir('.'):
    if os.path.isdir(f):
        for img in os.listdir(f):
            if img.endswith(".jpg"):
                label_name = img[:-4]+'.txt'
                label_path = os.path.join(label_dir,label_name)
                if os.path.exists(label_path):
                    os.rename(label_path,os.path.join(f,label_name))
                else:
                    print(f"Could not find labels for {img}")
            else:
                print('x',img)
    else:
        print('f',f)