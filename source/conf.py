from recommonmark.transform import AutoStructify
# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BTE NE'
copyright = '2022, vaporrrr'
author = 'vaporrrr'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'recommonmark',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx_panels'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None)
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

pygments_style = 'perldoc'
pygments_dark_style = 'monokai'

# -- Options for HTML output

html_theme = 'furo'
html_title = 'BTE Northeast Docs'
html_static_path = ['../_static']
html_favicon = '../_static/favicon.ico'
html_theme_options = {
    'sidebar_hide_name': True,
    'navigation_with_keys': True,
    'announcement': '<em>This site is a work in progress.</em>',
    'light_logo': 'nelogonew.png',
    'dark_logo': 'nelogonew.png',
    'light_css_variables': {
        'color-brand-primary': '#111111',
        'color-brand-content': '#0775C0',
        'color-admonition-background': '#F7F7F7'
    },
    'dark_css_variables': {
        'color-brand-primary': '#EEEEEE',
        'color-brand-content': '#2AC1FF',
        'color-admonition-background': '#383838'
    }
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_config_value('recommonmark_config', {
            #'url_resolver': lambda url: github_doc_root + url,
            'enable_math': False,
            'enable_inline_math': False,
            'enable_eval_rst': True,
        }, True)
    app.add_transform(AutoStructify)