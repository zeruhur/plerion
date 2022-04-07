for i in ../[0]*.md ; do $(pandoc -f gfm -t html -o html/$(basename ${i} .md).html $i) ; done
pandoc -t html -o pdf/plerion_ashcan.pdf -s html/*.html character_sheet.html --toc --toc-depth=1 --css="css/plerion.css" --metadata-file=metadata.yml --template=template/template.html --pdf-engine=weasyprint
rm html/*.html