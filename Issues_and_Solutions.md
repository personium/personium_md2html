# Issues & Solutions  
1. Pandoc cannot convert a link's URL as expected.  
Therefore, I use panflute to solve the following problem.  

    - Markdown:  

            [Document](./document.md)

    - Converted HTML:  

            <a href="./document.md">Document</a>

    - Expected HTML:  

            <a href="./document.html">Document</a>
