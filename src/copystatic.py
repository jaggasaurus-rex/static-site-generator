import shutil
import os

def source_to_destination():
    source_path = "static"
    dest_path = "public"
    print("Deleting public directory...")
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)
    print("Copying statc files to public directory...")
    if os.path.exists(source_path):
        new_directory_generator(source_path,dest_path)

def new_directory_generator(source_path,dest_path):
    if os.path.isfile(source_path):
        print(f" * {source_path} -> {dest_path}")
        shutil.copy(source_path,dest_path)
    elif os.path.isdir(source_path):
        sub_source = os.listdir(source_path)
        for item in sub_source:
            new_source_path = os.path.join(source_path,item)
            new_dest_path = os.path.join(dest_path,item)
            if os.path.isdir(new_source_path):
                os.mkdir(new_dest_path)
            new_directory_generator(new_source_path,new_dest_path)