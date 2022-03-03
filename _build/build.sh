pandoc -f gfm -t html -o pdf/plerion.pdf -s md/plerion.md --pdf-engine=weasyprint --css="css/plerion.css" --metadata pagetitle="Plerion" --columns=2
#--author="CC-BY-SA-4.0 Roberto Bisceglie"