
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lecture}

\gdef\outputtype{present}

\DeclareOption{draft}{\PassOptionsToClass{draft}{beamer}}
\DeclareOption{handout}{\PassOptionsToClass{handout}{beamer}\gdef\outputtype{handout}}
\DeclareOption{notes}{\PassOptionsToClass{handout}{beamer}\gdef\outputtype{notes}}
\ProcessOptions

\RequirePackage{colours}

\LoadClass[hyperref={
  colorlinks=true,
  urlcolor=usydblue,
  menucolor=black,
  pagecolor=black,
  linkcolor=black}
]{beamer}[3.06]
% need to fix the fact that this doesn't produce scalable quote chars
\RequirePackage{textcomp}
%\RequirePackage{pdffonts}
\RequirePackage{ifthen}
\RequirePackage{pgfpages}
\RequirePackage{tikz}
\RequirePackage{xspace}
\RequirePackage{listings}
\RequirePackage{pylistings}
\RequirePackage{vbalistings}
\RequirePackage{shelllistings}
\RequirePackage{sqllistings}
\RequirePackage{htmllistings}
\RequirePackage{latexlistings}
\RequirePackage{multimedia}

\input{names}

\setlength{\pyleftmargin}{0mm}
\setlength{\vbaleftmargin}{0mm}
\setlength{\sqlleftmargin}{0mm}
\setlength{\shellleftmargin}{0mm}
\setlength{\shelltopmargin}{1mm}
\setlength{\htmlleftmargin}{0mm}
\setlength{\latexleftmargin}{0mm}

\ifthenelse{\equal{\outputtype}{present}}{\relax}{
  % for both handout and notes
  \pgfpagesuselayout{4 on 1}[a4paper,landscape,border shrink=10mm]
  % just for notes
  \ifthenelse{\equal{\outputtype}{notes}}{
    \setbeameroption{show notes}
    \setbeamertemplate{note page}[plain]
  }{\relax}
}

\usetheme{USYD}

\author{James Curran and Tara Murphy}

\newcommand{\notetitle}[1]{\note{\textbf{\large #1}\\}}

\newcommand{\titleslide}{%
\begin{frame}[plain]%
\notetitle{\inserttitle}%
\titlepage%
\end{frame}%
}

\newcommand{\partslide}{%
\begin{frame}[plain]%
\notetitle{\insertpart}%
\partpage%
\end{frame}%
}

\newcommand{\outlineslide}{%
\begin{frame}
\frametitle{Outline}
\notetitle{Outline}%
\tableofcontents
\end{frame}
}

\newenvironment{plain}[1]{%
\subsection*{#1}
\begin{frame}[t,fragile,environment=plain]
\frametitle{#1}
\notetitle{#1}
\newcommand{\p}{\item}
}{%
\end{frame}
}

\newcommand{\stoppoints}{\end{itemize}}

\newenvironment{points}[1]{%
\subsection*{#1}
\begin{frame}[t,fragile,environment=points]
\frametitle{#1}
\notetitle{#1}
\newcommand{\p}{\item}
\begin{itemize}
}{%
\stoppoints
\end{frame}
}

\newcommand{\stopenums}{\end{enumerate}}

\newenvironment{enums}[1]{%
\subsection*{#1}
\begin{frame}[t,fragile,environment=enums]
\frametitle{#1}
\notetitle{#1}
\newcommand{\p}{\item}
\begin{enumerate}
}{%
\stopenums
\end{frame}
}

\newcommand{\stopcenter}{\end{center}}

\newenvironment{centre}[1]{%
\subsection*{#1}
\begin{frame}[t,fragile,environment=centre]
\frametitle{#1}
\notetitle{#1}
\newcommand{\p}{\item}%
\begin{center}
}{%
\stopcenter
\end{frame}
}

\newenvironment{video}[3]{%
\subsection*{#1}
\begin{frame}[t,fragile,environment=video]
\frametitle{#1}
\notetitle{#1}
\newcommand{\p}{\item}%
\begin{center}
\ifthenelse{\equal{\outputtype}{present}}{%
\movie[showcontrols=true,autostart,width=50mm,height=50mm]{#2}{#3}}{\relax}
}{%
\stopcenter
\end{frame}
}

\renewenvironment{quote}
                 {\begin{beamercolorbox}[rounded=true]{colour box}}
                 {\end{beamercolorbox}}

\newenvironment{pquote}
            {\begin{beamercolorbox}[rounded=true,wd=.85\textwidth]{colour box}}
            {\end{beamercolorbox}}

