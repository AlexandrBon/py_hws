FROM ubuntu:focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y texlive-latex-base python3

COPY . .

RUN apt install -y pip && pip install latex_gen_3000

RUN python3 task2/main.py > example.tex && pdflatex example.tex
