# pelican-github-releases
A pelican plugin to create pages based on github releases

# Configure the plugin

<pre>
GITHUB_RELEASE_URL = 'https://api.github.com/repos/mickem/nscp/releases'
GITHUB_MAJOR_VERSIONS = [ '0.4.3', '0.4.4']
GITHUB_PROMOTED_VERSION = '0.4.3.143'
GITHUB_RELEASE_SAVE_AS = 'download/{version}/index.html'
GITHUB_RELEASE_PROMOTED_SAVE_AS = 'download/index.html'
</pre>

* GITHUB_RELEASE_URL
  The github repository API URL. 
* GITHUB_MAJOR_VERSIONS
  A list of major versions to create (these will become a pages each with all revisions on them)
* GITHUB_PROMOTED_VERSION
  The "latest" releas which will be promoted on a special page
* GITHUB_RELEASE_SAVE_AS
  Where to save releases {version} will correspond with the various GITHUB_MAJOR_VERSIONS
* GITHUB_RELEASE_PROMOTED_SAVE_AS
  Where to save the "promoted release" i.e the normal download page.

# Creating templates

This plugin requires 2 templates one for releases and one for the promotes release.
For an example see the sample-template folder.

# Sample

To see this plugin in action see: 

* Promotd release: https://www.nsclient.org/download/
* Regular release: https://www.nsclient.org/download/0.4.3/
