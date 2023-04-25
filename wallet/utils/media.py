def image_upload_path(instance, file_name):
    file_folder = "Profile_images"
    return f"{file_folder}/{instance.username}/{file_name}"


def default_profile_image():
    return "default/user-default.png"
