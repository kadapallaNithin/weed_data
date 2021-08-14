import os 
target_dir = "../dataset"
classwise_dir = "."
#try:
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Created target directory')
images_dir = os.path.join(target_dir,"images")
labels_dir = os.path.join(target_dir,"labels")
images_train_dir = os.path.join(images_dir,"train")
images_test_dir = os.path.join(images_dir,"test")
labels_train_dir = os.path.join(labels_dir,"train")
labels_test_dir = os.path.join(labels_dir,"test")
os.mkdir(images_dir)
os.mkdir(labels_dir)
os.mkdir(images_train_dir)
os.mkdir(images_test_dir)
os.mkdir(labels_train_dir)
os.mkdir(labels_test_dir)

classes = ["hizda","bendalam","odipili","erra","gunjara","jiluga","jonna","x","paddy","a","janumu] #[]
# class_index = -1
os.chdir(classwise_dir)
for dir in classes:#os.listdir('.'):
    if os.path.isdir(dir):
        # if not f in classes:
        # classes.append(dir)
        # class_index += 1
        for img in os.listdir(dir):
            if img.endswith(".jpg"):
                img_path = os.path.join(dir,img)
                target_img_path = os.path.join(images_train_dir,img)
                label_name = img[:-4]+".txt"
                label_path = os.path.join(dir,label_name)
                if os.path.exists(label_path):
                    data = str(class_index) + open(label_path).read().replace("\n0 ","\n"+str(class_index)+" ")[1:]
                    f = open(os.path.join(labels_train_dir,label_name),'w')
                    f.write(data)
                    f.close()
                    os.system(f"cp {img_path} {target_img_path}")
                else:
                    print(f"Could not find labels for {dir}/{img}")
# f = open(os.path.join(labels_train_dir,"classes.txt"),'w')
# for c in classes:
#     f.write(c+"\n")
# f.close()
with open('custom.yaml','w') as f:
    f.write("train: "+images_train_dir+"\nval:"+images_test_dir+"\nnc: "+str(len(classes))+"\nclasses:"+str(classes))