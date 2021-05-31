from urllib.parse import urlparse
from flask import render_template, url_for, send_from_directory, request, make_response
from app import app
from app.models import Post, PostType
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.order_by(Post.timestamp.desc()).filter_by(post_type=PostType.POSTER).all()
    if post is None:
        return render_template('error.html', 'Posters not present')

    return render_template('index.html', posts=posts)

@main.route('/post/<int:id>/<string:header>', methods=['GET', 'POST'])
def post(id, header):
    if id < 0:
        return render_template('error.html', 'Post not present')

    page = Post.query.get_or_404(id)
    if page is None:
        return render_template('error.html', 'Post {:s} not present'.format(id))

    return render_template('post.html', post=page)

@main.route('/download_file/<int:id>/<filename>', methods=['GET'])
def download_file(id, filename):
    directory = '{:s}/{:s}'.format(app.config['UPLOAD_FOLDER'], str(id))
    return send_from_directory(directory, filename)

@main.route("/sitemap")
@main.route("/sitemap/")
@main.route("/sitemap.xml")
def sitemap():
    """
        Route to dynamically generate a sitemap of your website/application.
        lastmod and priority tags omitted on static pages.
        lastmod included on dynamic content such as blog posts.
    """
    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc

    static_url_list = {'home':'main.index'}
    # Static routes with static content
    static_urls = list()
    for key, value in static_url_list.items():
        print('rule:', key, value)
        url = {
            "loc": "{}/{}".format(host_base, url_for(value))
        }
        static_urls.append(url)

    # Dynamic routes with dynamic content
    dynamic_urls = list()
    blog_posts = Post.query.all()
    for post in blog_posts:
        url_ext = url_for('main.post', id=post.id, header=post.header)

        url = {
            "loc": "{}/{}".format(host_base, url_ext),
            "lastmod": post.timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        dynamic_urls.append(url)

    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls, host_base=host_base)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response
