# this config and custom css reference qian-gu.github.io settings
AUTHOR = 'winter'
SITENAME = "Sumarization"
SITEURL = "https://wantong.github.io"

SITETITLE = AUTHOR
SITESUBTITLE = u"concentrate"
SITEDESCRIPTION = "Tight your thought, fast your work flow"
SITELOGO = SITEURL + '/images/toppicture.png'
FAVICON = SITEURL + '/images/web_icon_64x64.icon'
BROWSER_COLOR = '#333333'
RELATIVE_URLS = True

SOCIAL = (('envelope', 'mailto:liwantong@163.com'),
    ('github','https://github.com/wantong'),
        )

MENUITEMS = (('Authors', '/authors.html'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             )

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'          # 默�?��??言设为�?�?
OG_LOCALE = 'zh_CN'          # Open Graph 元数�?�?言
LOCALE = 'zh_CN.UTF-8'       # �?地化设置（确保系统已安�?��?��??言包）

BIND = "0.0.0.0"  # 允�?��?�部访问
PORT = 3588          # 指定�?�?

THEME = 'Flex'
THEME_COLOR = 'light'

PLUGIN_PATHS = ['../pelican-pluginss']
PLUGINS = ['i18n_subsites',  'neighbors',  'related_posts',
           'sitemap', 'representative_image', 'render_math',
           'series',]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# dark mode
THEME_COLOR = 'ligtht'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'monokai'
PYGMENTS_STYLE_DARK = 'monokai'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# pelicanconf.py

CJK_AUTO_SPAING_TITLE = True
ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2025

#  STATIC_PATHS = ["extra/custom.css"]

# Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

MAIN_MENU = True

MARKDOWN = {
    "extension_configs": {
        # Needed for code syntax highlighting
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.admonition": {},
        # This is for enabling the TOC generation
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
STATIC_PATHS = ['images', 'files', 'extra/custom.css']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'
