fast:
	pdflatex slides

all: slides.pdf notes.pdf handout.pdf

slides.pdf: .force slides.tex
	latex slides
	latex slides
	dvipdfm slides

notes.pdf: notes.tex lecture.tex
	pdflatex notes
	pdflatex notes

handout.pdf: handout.tex lecture.tex
	pdflatex handout
	pdflatex handout

draft.pdf: draft.tex lecture.tex
	pdflatex draft
	pdflatex draft

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb *.idx *~

.force:
