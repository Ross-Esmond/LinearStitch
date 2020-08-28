# LinearStitch #

LinearStitch is a very simple image stitcher designed for images show in a single horizontal line, from left to right, using something like a [Gigamacro](http://www.gigamacro.com).  

LinearStitch uses SIFT to identify matches between the likely-overlap regions of two images.  It then directly concatenates those images together (without blending).  The goal is to ensure that the original images are undistorted, even if that means the stitch seam itself is imperfect.

To run LinearStitch, you'll need to have Python3 and OpenCV 3, along with a few python dependencies.  For instructions for installtion Python3 and OpenCV3 on the Mac, visit [http://seeb0h.github.io/howto/howto-install-homebrew-python-opencv-osx-el-capitan/](http://seeb0h.github.io/howto/howto-install-homebrew-python-opencv-osx-el-capitan/).  

To install on Windows, we recommend using [Anaconda](http://anaconda.org).  [These instructions](https://rivercitylabs.org/up-and-running-with-opencv3-and-python-3-anaconda-edition/) will walk you through the process.  Uee conda install -c menpo opencv to get the proper verison of opencv (3.4).

In additon to OpenCV, you'll need tkinter and numpy installed.  Both of these can be installed via pip.

For more information on this software, please visit [labs.latis.umn.edu](http://labs.latis.umn.edu).

### Configuration

A sample config file is included: `config.sample.ini`. To start configuring LinearStitch immediately, you may rename `config.sample.ini` to `config.ini`, and update settings there. Most options are documented inside the config file. One option to consider is the ArchivePath, where zipped copies of image directories will be deposited after they are processed.

Whenever `LS_GUI.py` is run, LinearStitch will check for a `config.ini` file. If there is no config, one will be created by copying `config.sample.ini`. This is simply a convenience for fresh installs. An existing `config.ini` will never be overridden.
