import json
import logging
from flask import Blueprint, render_template, request
from main.dao.post_dao import PostDAO
from config import POST_PATH_POSTS

info_loger = logging.getLogger("info_logger")
error_logger = logging.getLogger("error_logger")
main = Blueprint('main',__name__)

postDAO = PostDAO(POST_PATH_POSTS)



@main.route('/')
def page_index():
    return render_template('index.html')

@main.route('/search/')
def get_search():
    s = request.args["s"]
    info_loger.info(f"Поиск по строке {s}")
    error_logger.error(f"Поиск по строке {s}")
    posts = postDAO.get_searcg(s)
    return render_template('post.html', items=posts, name=s)