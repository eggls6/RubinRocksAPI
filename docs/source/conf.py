# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Rubin Rocks"
copyright = '2026 UIUC'
author = 'Samuel Cornwall, Siegfried Eggl, Sarah Greenstreet, Dmitrii Vavilov'

release = '0.2'
version = '0.1.1'

# -- General configuration

extensions = [

    # Built-in

    "sphinx.ext.autodoc",

    "sphinx.ext.autosummary",

    "sphinx.ext.napoleon",

    "sphinx.ext.intersphinx",

    "sphinx.ext.viewcode",

    "sphinx.ext.todo",

    "sphinx.ext.duration",

    "sphinx.ext.coverage",

    # Third-party

    "sphinx_design",

    "sphinxcontrib.mermaid",
    
    "sphinxcontrib.httpdomain",
]    

templates_path = ["_templates"]

exclude_patterns = [

    "_build",

    "Thumbs.db",

    ".DS_Store",

]

source_suffix = {

    ".rst": "restructuredtext",

}

master_doc = "index"

language = "en"

# -----------------------------------------------------------------------------

# Autodoc

# -----------------------------------------------------------------------------

autosummary_generate = True

autoclass_content = "both"

autodoc_default_options = {

    "members": True,

    "undoc-members": False,

    "show-inheritance": True,

}

autodoc_typehints = "description"

# -----------------------------------------------------------------------------

# Napoleon (Google / NumPy docstrings)

# -----------------------------------------------------------------------------

napoleon_google_docstring = True

napoleon_numpy_docstring = True

# -----------------------------------------------------------------------------

# Intersphinx

# -----------------------------------------------------------------------------

intersphinx_mapping = {

    "python": ("https://docs.python.org/3", None),

    "numpy": ("https://numpy.org/doc/stable/", None),

}

# -----------------------------------------------------------------------------

# TODOs

# -----------------------------------------------------------------------------

todo_include_todos = False

# -----------------------------------------------------------------------------

# HTML output

# -----------------------------------------------------------------------------

html_theme = "furo"

html_title = project

html_static_path = ["_static"]

html_css_files = ["custom.css"]

templates_path = ["_templates"]

html_logo = "_static/logonsf.png"

#html_favicon = "_static/favicon.ico"


# -----------------------------------------------------------------------------

# GitHub links

# -----------------------------------------------------------------------------

html_context = {

    "display_github": True,

    "github_user": "eggls6",

    "github_repo": "RubinRocksAPI",

    "github_version": "main",

    "conf_py_path": "/docs/",

}

# -----------------------------------------------------------------------------

# Copybutton

# -----------------------------------------------------------------------------

copybutton_prompt_text = r">>> |\.\.\. |\$ "

copybutton_prompt_is_regexp = True

# -----------------------------------------------------------------------------

# Mermaid

# -----------------------------------------------------------------------------

mermaid_version = "11.0.0"

# -----------------------------------------------------------------------------

# Warnings

# -----------------------------------------------------------------------------

nitpicky = True

# extensions = [
#     'sphinx_code_tabs',
#     'sphinxcontrib.httpdomain',
#     'sphinx.ext.duration',
#     'sphinx.ext.doctest',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.intersphinx',
#     'sphinx_tabs.tabs'
# ]

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

# templates_path = ['_templates']

# # -- Options for HTML output

# # html_theme = 'sphinx_rtd_theme'
# html_theme = 'furo'

# # -- Options for EPUB output
# epub_show_urls = 'footnote'
