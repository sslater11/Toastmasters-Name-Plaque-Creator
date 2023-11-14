#!/usr/bin/env python3

# Copyright (C) 2023  Simon Slater
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import sys

DEFAULT_FONT_SIZE = 140
are_fold_lines_visible = True
toastmasters_html_filename = "toastmasters_name_plaques.html"
toastmasters_names_filename = "toastmasters.txt"


html_start = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Toastmasters - Name Printout</title>
    <!-- Normalize or reset CSS with your favorite library -->
<!--
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css">
-->

    <!-- Load paper.css for happy printing -->
<!--
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/paper-css/0.4.1/paper.css">
-->
    <!-- Set page size here: A5, A4 or A3 -->
    <!-- Set also "landscape" if you need -->
    <style>
/*! normalize.css v7.0.0 | MIT License | github.com/necolas/normalize.css */html{line-height:1.15;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,footer,header,nav,section{display:block}h1{font-size:2em;margin:.67em 0}figcaption,figure,main{display:block}figure{margin:1em 40px}hr{box-sizing:content-box;height:0;overflow:visible}pre{font-family:monospace,monospace;font-size:1em}a{background-color:transparent;-webkit-text-decoration-skip:objects}abbr[title]{border-bottom:none;text-decoration:underline;text-decoration:underline dotted}b,strong{font-weight:inherit}b,strong{font-weight:bolder}code,kbd,samp{font-family:monospace,monospace;font-size:1em}dfn{font-style:italic}mark{background-color:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}audio,video{display:inline-block}audio:not([controls]){display:none;height:0}img{border-style:none}svg:not(:root){overflow:hidden}button,input,optgroup,select,textarea{font-family:sans-serif;font-size:100%;line-height:1.15;margin:0}button,input{overflow:visible}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{border-style:none;padding:0}[type=button]:-moz-focusring,[type=reset]:-moz-focusring,[type=submit]:-moz-focusring,button:-moz-focusring{outline:1px dotted ButtonText}fieldset{padding:.35em .75em .625em}legend{box-sizing:border-box;color:inherit;display:table;max-width:100%;padding:0;white-space:normal}progress{display:inline-block;vertical-align:baseline}textarea{overflow:auto}[type=checkbox],[type=radio]{box-sizing:border-box;padding:0}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}details,menu{display:block}summary{display:list-item}canvas{display:inline-block}template{display:none}[hidden]{display:none}/*# sourceMappingURL=normalize.min.css.map */

    /* copied directly from css from paper-css at "https://cdnjs.cloudflare.com/ajax/libs/paper-css/0.4.1/paper.css" */
    /* Paper-css Start */
    /* The ISC Licence applys to just this paper-css section */
/*
ISC Licence

Copyright (c) 2017–2018, Rhyne Vlaservich rhyneav@gmail.com

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
*/
    /* Load paper.css for happy printing */
@page { margin: 0 }
body { margin: 0 }
.sheet {
  margin: 0;
  overflow: hidden;
  position: relative;
  box-sizing: border-box;
  page-break-after: always;
}

/** Paper sizes **/
body.A3               .sheet { width: 297mm; height: 419mm }
body.A3.landscape     .sheet { width: 420mm; height: 296mm }
body.A4               .sheet { width: 210mm; height: 296mm }
body.A4.landscape     .sheet { width: 297mm; height: 209mm }
body.A5               .sheet { width: 148mm; height: 209mm }
body.A5.landscape     .sheet { width: 210mm; height: 147mm }
body.letter           .sheet { width: 216mm; height: 279mm }
body.letter.landscape .sheet { width: 280mm; height: 215mm }
body.legal            .sheet { width: 216mm; height: 356mm }
body.legal.landscape  .sheet { width: 357mm; height: 215mm }

/** Padding area **/
.sheet.padding-10mm { padding: 10mm }
.sheet.padding-15mm { padding: 15mm }
.sheet.padding-20mm { padding: 20mm }
.sheet.padding-25mm { padding: 25mm }

/** For screen preview **/
@media screen {
  body { background: #e0e0e0 }
  .sheet {
    background: white;
    box-shadow: 0 .5mm 2mm rgba(0,0,0,.3);
    margin: 5mm auto;
  }
}

/** Fix for Chrome issue #273306 **/
@media print {
           body.A3.landscape { width: 420mm }
  body.A3, body.A4.landscape { width: 297mm }
  body.A4, body.A5.landscape { width: 210mm }
  body.A5                    { width: 148mm }
  body.letter, body.legal    { width: 216mm }
  body.letter.landscape      { width: 280mm }
  body.legal.landscape       { width: 357mm }
}
    /* Set page size here: A5, A4 or A3 */
    /* Set also "landscape" if you need */
    /* Paper-css End*/


@media print {
   .sheet {
         /* firefox, safari extra page fix */
                              }
                              }

        @page { size: A4 landscape; }
        @media screen, print {
            body{ font-size: 10px; font-family: Arial, sans-serif;}
            .toastmastersTable { width: 100%; height: 50%; border: 0; }
            .toastmastersTableRow { width: 100%; height: 50%; border: 0; }
            .toastmastersTableRowUpsidedown { width: 100%; height: 50%; border: 0; transform: rotate(180deg); }

            .toastmastersTableCellImageWithoutFoldLines { overflow:hidden; width: 1%; border-width: 0px 0px 0px 0px; vertical-align:middle; text-align:center; padding: 30px 0px 0px 0px; }
            .toastmastersTableCellImageUpsidedownWithoutFoldLines { overflow:hidden; width: 1%; border-width: 0px 0px 0px 0px; vertical-align:middle; text-align:center; padding: 30px 0px 0px 0px; transform: rotate(180deg); }

            .toastmastersTableCellImage { overflow:hidden; width: 1%; border-width: 1px 0px 0px 0px; border-style: dashed; vertical-align:middle; text-align:center; padding: 30px 0px 0px 0px; }
            .toastmastersTableCellImageUpsidedown { overflow:hidden; width: 1%; border-width: 1px 0px 0px 0px; border-style: dashed; vertical-align:middle; text-align:center; padding: 30px 0px 0px 0px; transform: rotate(180deg); }
        }
    </style>
</head>

<!-- Set "A5", "A4" or "A3" for class name -->
<!-- Set also "landscape" if you need -->
<body class="A4 landscape" >
    <!-- Each sheet element should have the class "sheet" -->
    <!-- "padding-**mm" is optional: you can set 10, 15, 20 or 25 -->

"""


html_end = """
</body>
</html>"""


one_page_without_fold_lines = """
<section class="sheet padding-10mm">
    <!-- Write HTML just like a web page -->
    <page size="A4 landscape">
    <table id="text_cell" class="toastmastersTable" >
    <thead></thead>
    <tbody>
        <tr class="toastmastersTableRow" >
          <td style="font-size: 140px; border-width: 0px 0px 0px 0px; vertical-align:middle; text-align:center; transform: rotate(180deg);" }>

          <b>Simon</b>
          </td>
          <td class="toastmastersTableCellImageUpsidedownWithoutFoldLines">
              <img src="https://toastmasterscdn.azureedge.net/medias/images/brand-items/color-logo.jpg" style="width: 277px; height: 242px" >
          </td>
        </tr>
    </tbody>
    </table>
    <table id="text_cell" class="toastmastersTable" >
    <thead></thead>
    <tbody>
        <tr class="toastmastersTableRow" >
          <td class="toastmastersTableCellImageWithoutFoldLines">
              <img src="https://toastmasterscdn.azureedge.net/medias/images/brand-items/color-logo.jpg" style="width: 277px; height: 242px" >
          </td>
          <td style="font-size: 140px; border-width: 0px 0px 0px 0px; vertical-align:middle; text-align:center;" }>
                  <b>Simon</b>
          </td>
        </tr>
    </tbody>
    </table>
</section>    <!-- Each sheet element should have the class "sheet" -->
"""

one_page_with_fold_lines = """
<section class="sheet padding-10mm">
    <!-- Write HTML just like a web page -->
    <page size="A4 landscape">
    <table id="text_cell" class="toastmastersTable" >
    <thead></thead>
    <tbody>
        <tr class="toastmastersTableRow" >
          <td style="font-size: 140px; border-width: 1px 0px 0px 0px; border-style: dashed; vertical-align:middle; text-align:center; transform: rotate(180deg);" }>

          <b>Simon</b>
          </td>
          <td class="toastmastersTableCellImageUpsidedown">
              <img src="https://toastmasterscdn.azureedge.net/medias/images/brand-items/color-logo.jpg" style="width: 277px; height: 242px" >
          </td>
        </tr>
    </tbody>
    </table>
    <table id="text_cell" class="toastmastersTable" >
    <thead></thead>
    <tbody>
        <tr class="toastmastersTableRow" >
          <td class="toastmastersTableCellImage">
              <img src="https://toastmasterscdn.azureedge.net/medias/images/brand-items/color-logo.jpg" style="width: 277px; height: 242px" >
          </td>
          <td style="font-size: 140px; border-width: 1px 0px 0px 0px; border-style: dashed; vertical-align:middle; text-align:center;" }>
                  <b>Simon</b>
          </td>
        </tr>
    </tbody>
    </table>
</section>    <!-- Each sheet element should have the class "sheet" -->
"""



def create_page( name, font_size = DEFAULT_FONT_SIZE ):
    if are_fold_lines_visible:
        toastmasters_page =    one_page_with_fold_lines.replace("Simon", name)
    else:
        toastmasters_page = one_page_without_fold_lines.replace("Simon", name)

    toastmasters_page = toastmasters_page.replace("font-size: 140", "font-size: " + str(font_size))

    return toastmasters_page



def help():
    print("Read the README.md for how to use this.")
    print("It's really simple. Edit the toastmasters.txt file, adding all members and their titles.")
    print("Run this script.")
    print("Open the " + toastmasters_html_filename + " file and print out all the name plaques onto A4 card.")
    print("Arguments:")
    print("\t--without-fold-lines - This will create a page without the dashed fold lines.")
    exit()

def main( args ):
    if len( args ) > 1:
        if (args[1] == "--help") or (args[1] == "-h"):
            help()
            exit()
        if args[1] == "--without-fold-lines":
            global are_fold_lines_visible
            are_fold_lines_visible = False


    toastmasters_html = open( toastmasters_html_filename, "w" )
    toastmasters_names_file = open(toastmasters_names_filename, "r")

    toastmasters_html.write( html_start )

    print( "Creating a name plaque for:" )
    # Create a page for every toastmaster.
    for line in toastmasters_names_file:
        line = line.strip()
        if (line == "") or ((len(line) > 0) and (line[0]=="#")):
            # It's a blank line or a commented out line in the file, so do nothing.
            continue

        # Name and font are separated by a comma.
        elements = line.split(",")
        if len( elements ) == 1:
            toastmasters_html.write( create_page( elements[0].strip() ) )
        if len( elements ) == 2:
            toastmasters_html.write( create_page( elements[0].strip(), elements[1].strip() ) )
        print(line)

    # Make a blank page for guests.
    toastmasters_html.write( create_page( "" ) )

    toastmasters_html.write( html_end )
    toastmasters_html.close()
    toastmasters_names_file.close()

    print( "" )
    print( "" )
    print( "" )
    print( "--- Finished ---" )
    print( "Created name plaques." )
    print( "Name plaques saved to: " + toastmasters_html_filename )

if __name__ == "__main__":
    main(sys.argv)

