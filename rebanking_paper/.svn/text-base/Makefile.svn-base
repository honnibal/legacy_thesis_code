paper:
	latex rebanking
	bibtex rebanking
	latex rebanking
	latex rebanking
	dvipdf rebanking

pdf:
	pdflatex rebanking
	bibtex rebanking
	pdflatex rebanking
	pdflatex rebanking
        scp rebanking.pdf mhonn@nlp4:lib/html/rebanking

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.idx *~ *.lot *.lof *.blg *.bbl *.dvi *.pdf

.force:
