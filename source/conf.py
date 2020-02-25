# -*- coding: utf-8 -*-
#
# Rsyslog Doc documentation build configuration file, created by
# sphinx-quickstart on Sun Apr 28 07:10:10 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys

# Module for our custom functions. Used with automating build info.
sys.path.append(os.getcwd())
import conf_helpers


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('_ext'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.5.1'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['edit_on_github', 'sphinx.ext.todo']
edit_on_github_project = 'rsyslog/rsyslog-doc'
edit_on_github_branch = 'master'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'rsyslog'
copyright = u'2008-2019, Rainer Gerhards and Others'
author = u'Rainer Gerhards and Others'


# https://stackoverflow.com/questions/26242919/sphinx-documentation-system-multiple-substitutions-with-rst-prolog
# http://www.sphinx-doc.org/en/stable/config.html#confval-rst_prolog
#
# This will be included at the beginning of every source file that is read.
#
# Note: We intentionally include a few substitution definitions directly
# so that the placeholders used here can be replaced by Python's
# string format method.
rst_prolog = """

.. |DOC_BUILD| replace:: ``{doc_build}``
.. |DOC_COMMIT| replace:: ``{doc_commit}``
.. |DOC_BRANCH| replace:: ``{doc_branch}``

.. include:: /includes/substitution_definitions.inc.rst

"""

# http://www.sphinx-doc.org/en/stable/config.html#confval-rst_epilog
# This will be included at the end of every source file that is read.
rst_epilog = """

.. include:: /includes/footer.inc.rst

"""





###############################################################################
# Placeholder/template values to be filled in by the release_build.sh script
#
# These values are filled in as part of preparing the official docs
# distribution tarball. If the placeholder values are left intact then
# real values will be generated dynamically from info in the repo. If the
# user builds the docs from "bare" sources not yet processed
###############################################################################
version = '8'
release = version + ' daily stable'


# For this to be true, it means that we are not attempting to build from
# a release tarball, as otherwise the values above would have been replaced
# with official stable release values.
if version == '8':

    # Confirm that a .git folder is available. If not, skip all
    # following steps intended to generate "dev" build values for
    # 'version' and 'release' build configuration variables. In that
    # case, keep the placeholder values already set.

    # The directory where this conf.py file is located
    source_conf_dir = os.getcwd()

    # If building from a Git repo, then this directory should be present
    # in the parent directory.
    git_dir = \
        os.path.abspath(os.path.join(os.getcwd(), os.pardir)) \
        + os.sep + '.git'

    if os.path.isdir(git_dir):

        # If the 'version' variable is left with a placeholder it means
        # that this build configuration is being called from a Git repo
        # and that we should pull info from the repo to dynamically
        # fill in values that were not specified by a build script.
        release_type = 'dev'

        # Valid options are "simple" and "detailed". "Simple" contains a short
        # dev build string intended for space constrained display. "Detailed"
        # contains a much longer dev build string intended for output that is
        # used for for copyediting/proofreading, where the generated docs may
        # hang around a while before being disposed of. In that situation,
        # having detailed build details in the doc are useful to help
        # differentiate multiple document builds (even from different branches)
        # from each other.
        #release_string_detail = 'detailed'
        release_string_detail = 'simple'

        # Some items in the source are wrapped with the ".. only:: TAG_NAME_HERE"
        # Sphinx directive. This directive prevents the wrapped block of markup
        # from being processed unless the specified tag is set. Using this approach
        # helps to specific content from being included in stable release docs
        # that is only intended for dev/review copies of the documentation.
        tags.add(release_type)

        # The version info for the project you're documenting, acts as replacement for
        # |version| and |release|, also used in various other places throughout the
        # built documents.
        #
        # The short X.Y version.
        version = conf_helpers.get_next_stable_version()

        # This is displayed in multiple prominent locations in the docs
        # where it is useful to be able to tell at a glance when the files
        # were generated and from what commit.
        #
        # The full version, including alpha/beta/rc tags.
        release = conf_helpers.get_release_string(
            release_type,
            release_string_detail,
            version)


        # Additions that are used by dev builds
        rst_prolog = rst_prolog.format(
            doc_build=release,
            doc_commit=conf_helpers.get_current_commit_hash(),
            doc_branch=conf_helpers.get_current_branch()
        )

# Disable use of dev build logic, fall back to standard release string values.
else:
    release_type = 'stable'


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
#
# Note: We list the *.inc.rst filename pattern here so that matching
# files will not be parsed as separate files to include directly into
# the documentation structure in addition to them being pulled in via
# include statements. Even with include files having been moved to the
# 'source/includes' directory the wildcard pattern has been kept to
# help rule out any issues should an include file be purposely moved
# to the root of the 'source' directory (seen a '/' by Sphinx).
exclude_patterns = ['*.inc.rst', 'includes']


# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Warn about all references where the target cannot be found. Default is False.
nitpicky = True

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# If this is True, todo emits a warning for each TODO entries. The default
# is False.
todo_emit_warnings = True

# Supress "unknown mimetype for ..." warnings
suppress_warnings = ['epub.unknown_project_files']

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'
#html_theme = 'basic'
#html_style = 'rsyslog.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
if release_type == 'dev':

    html_title = "{} {} docs".format(
        project,
        conf_helpers.get_release_string(
            release_type, release_string_detail, version)
    )

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'rsyslogdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'RsyslogDoc.tex', u'Rsyslog Doc Documentation',
   u'foo bar', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('queues', 'rsyslog-queues', u'Rsyslog Documentation: Queues',
     [u'Rainer Gerhards'], 1),
    ('configuration/actions', 'rsyslog-actions', u'Rsyslog Documentation: Actions',
     [u'Rainer Gerhards'], 1),
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'RsyslogDoc', u'Rsyslog Doc Documentation',
   u'foo bar', 'RsyslogDoc', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


# -- Options for epub output ---------------------------------------------------

# Use detailed build strings for epub format IF this is a dev build
# and NOT a stable build (which does not use detailed release strings)
if release_type == 'dev':

    # Override "simple" dev build string for epub format
    release_string_detail = 'detailed'

    epub_title = "{} {} docs".format(
        project,
        conf_helpers.get_release_string(
            release_type,
            release_string_detail, version
        )
    )

epub_theme = 'epub'
epub_basename = project
epub_author = author
epub_contributor = u'Rsyslog Community'
epub_publisher = 'http://www.rsyslog.com/'
epub_description = u'Documentation for the rsyslog project'


# http://www.sphinx-doc.org/en/stable/extdev/appapi.html#sphinx.application.Sphinx.add_stylesheet
# Include our custom stylesheet in addition to specified theme
def setup(app):
    app.add_stylesheet('rsyslog.css')
