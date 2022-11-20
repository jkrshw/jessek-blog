Title: LaTeX \includegraphics causes font rendering problems
Date: 2012-03-13 10:20
Tags: gimp, LaTex
Slug: latex-includegraphics-causes-font

LaTeX \includegraphics causes font rendering problems
When using \includegraphics to add a png image to a LaTeX document the text following the image becomes bold and the rendering just looks wrong.

This turns out to be an issue with Adobe Reader not being able to handle the alpha channel of the png image. The solution is fortunately quite easy to resolve. Simply remove the alpha channel from the image. This can be done in gimp using the Layer -> Transparency -> Remove Alpha Channel menu option.

<http://groups.google.com/group/latexusersgroup/browse_thread/thread/d204b186c9cb0aeb>