import os
from PIL import Image
from flask import current_app

def add_profile_picture(pic_upload, username):
    
    filename = pic_upload.filename
    ext_name = filename.split(".")[-1]
    
    updated_name = f'{username}.{ext_name}'
    
    filepath = os.path.join(current_app.root_path, 'static\profile_pics', updated_name)
    
    output_size = (200,200)
    
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)
    
    return updated_name
    
    
