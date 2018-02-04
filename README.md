# Overview  
Tools for converting Personium document (Markdown format) to HTML files.  

# Issues & Solutions  
When converting Personium document to HTML, we encounter serveral problems.  
If you are interested, check [this](Issues_and_Solutions.md) out.  

# Installing personium_md2html  
Installation procedures are based on [ota-meshi's procedures](http://qiita.com/ota-meshi/items/50d1e2b06ce0fe46f1ae).  
It is quite easy. It took less than 15 minutes when I installed personium_md2html on my Windows 10.  

## Windows  
1. Down and install [Pandoc](https://github.com/jgm/pandoc/releases/tag/1.19.2.1)  
If you are stucked, please refer to the procedures on the official [Installing pandoc](https://pandoc.org/installing.html) site.  
1. Down and install [Python](https://www.python.org/downloads/windows/) because Panflute requies Python to run.
1. According to [Panflute's guide](http://scorreia.com/software/panflute/install.html) I executed the following command.    
    - no proxy  
    
            > pip install panflute
        
    - behind proxy  
    
            > pip install panflute --proxy http://<user id>:<password>@<proxy address>
            
1. I also install [pypandoc](https://pypi.python.org/pypi/pypandoc) so that I can avoid using external commands.  
    - no proxy  
    
            > pip install pypandoc
        
    - behind proxy  
    
            > pip install pypandoc --proxy http://<user id>:<password>@<proxy address>

1. Copy and paste the following [Python files](src/) to a specific folder.  
    1. convert_link.py
    1. personium_md2html.py

## Linux  
Basically the same procedures in Windows should work.  

### Extra configurations  
Must specify python library path in convert_link.py.  
[Sample file](src/convert_link.py.sample) for my Linux server.  

# Command  
By the way, this tool automatically converts README.md to index.html.  

## Usages  
An example when I ran display the help in Windows 10.  

    > python personium_md2html.py --help
    usage: personium_md2html.py [-h] [--locale {en,ja}]

    Convert markdown file(s) to HTML file(s) recursively in a directory where this
    command is executed.

    optional arguments:
      -h, --help        show this help message and exit
      --locale {en,ja}  Specify the locale of your github.css.

    >

## How it works  
1. Move to the directory that contains markdown file(s).  
1. Execute the following command.  
    - Default  

            > python <path to md2html folder>/personium_md2html.py 

    - To specify one CSS file (/default/personium.css)  
        
            > python <path to md2html folder>/E:\work\personium_md2html\src>python personium_md2html.py --css=/default/personium.css

    - To more CSS files (/default/personium.css and /default/en/personium.css)  

            > python <path to md2html folder>/E:\work\personium_md2html\src>python personium_md2html.py --css=/default/personium.css --css=/default/en/personium.css
            
## Advance example  
To specify the template for conversion.  
        > python personium_md2html.py --template=/default/templates/default.html" --css=/default/personium.css --css=/default/en/personium.css