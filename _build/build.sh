for i in ../[0]*.md ; do $(pandoc -f gfm -t html -o html/$(basename ${i} .md).html $i) ; done
pandoc -t html -o pdf/plerion_ashcan.pdf -s html/*.html --toc --toc-depth=1 --css="css/plerion.css" --metadata-file=metadata.yml --template=template/template.html --pdf-engine=weasyprint
# pandoc -t rtf -o text/plerion.rtf -s html/*.html
rm html/*.html