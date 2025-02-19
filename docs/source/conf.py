# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Tile Prefab Placer'
copyright = '2024, 604Spirit'
author = '604Spirit'

release = '1.1.0'
version = '1.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

tags.add('custom3')

# Options for LaTeX output
# ------------------------

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# remove blank pages (between the title page and the TOC, etc.)
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}