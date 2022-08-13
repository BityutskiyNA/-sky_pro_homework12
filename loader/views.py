import logging
from flask import Blueprint, render_template, request, send_from_directory

from config import POST_PATH_POSTS
from main.dao.post_dao import PostDAO

postDAO = PostDAO(POST_PATH_POSTS)
loader = Blueprint('loader',__name__)
info_loger = logging.getLogger("info_logger")
error_logger = logging.getLogger("error_logger")

@loader.route('/posts/')
def page_index():
    return render_template('post_form.html')


@loader.route('/posts/post_uploaded', methods=['POST'])
def post_uploaded():
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    picture = request.files.get("picture")
    if picture:
        filename = picture.filename
        extension = filename.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            file_picture = f"/uploads/images/{filename}"
            picture.save(f"./uploads/images/{filename}")
            content = request.form["content"]
            postDAO.add_post(file_picture, content)
            return render_template('post_uploaded.html', content=content, picture=file_picture)
        else:
            info_loger.info(f"Формат файла не поддерживатеся {extension}")
            return f"Формат файла не поддерживатеся {extension}"
    else:
        error_logger.error("Файл не загружен")
        return "Файл не загружен"




@loader.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)

