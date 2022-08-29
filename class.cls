\LoadClass{article}

% math and physics
\RequirePackage{amssymb}
\RequirePackage{amsmath}
\RequirePackage{amsthm}
\RequirePackage{amsfonts}
\RequirePackage{mathtools}
\RequirePackage{physics}

% general
\RequirePackage[a-1b]{pdfx}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[british]{babel}
\RequirePackage{changepage}
\RequirePackage{enumitem}
\RequirePackage{abstract}
\RequirePackage{ifthen}
\RequirePackage[noabbrev,capitalize]{cleveref}
\RequirePackage{biblatex}
\RequirePackage{geometry}
\RequirePackage{minted}
\RequirePackage{csquotes}

% graphic
\PassOptionsToPackage{table,
                      dvipsnames,
                      x11names,
                      svgnames,
                      rgb,
                      hyperref}{xcolor}
\hypersetup{colorlinks=true,
            linkcolor=midnightblue,
            anchorcolor=midnightblue,
            citecolor=midnightblue,
            filecolor=midnightblue,
            urlcolor=midnightblue}
\definecolor{midnightblue}{HTML}{191970}
\RequirePackage[font=sc, labelsep=endash]{caption}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage{booktabs}
\usetikzlibrary{shapes, arrows, intersections}
\RequirePackage{animate}
\renewcommand{\arraystretch}{1.2}

% variables, constants, symbols
\DeclareMathOperator{\Ker}{Ker}
\DeclareMathOperator{\Ran}{Ran}
\DeclareMathOperator{\lin}{lin}
\renewcommand{\phi}{\varphi}
\renewcommand{\epsilon}{\varepsilon}
\renewcommand{\H}{\mathcal{H}}
\newcommand{\F}{\mathcal{F}}
\newcommand{\id}{\mathbb{I}}
\renewcommand{\S}{\mathcal{S}}
\newcommand{\Hd}{\dot H}
\newcommand{\Ci}{C^\infty}
\newcommand{\Li}{L^\infty}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\tilde{C}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Np}{\mathbb{N}^+}
\newcommand{\D}{\mathbb{D}}
\newcommand{\K}{\mathbb{K}}
\newcommand{\jb}[1]{\left\langle#1\right\rangle}

% theorem environments
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}{Corollary}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{proposition}{Proposition}[section]
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\theoremstyle{remark}
\newtheorem{remark}{Remark}
\newtheorem{example}{Example}