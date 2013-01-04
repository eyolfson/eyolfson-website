all: ../static/images/favicon.ico ../static/images/logo.png

../static/images/favicon.ico: favicon.tex
	@echo "[XELATEX] $<"
	@xelatex -interaction=nonstopmode -shell-escape $< &> /dev/null
	@echo "[CONVERT] $(<:.tex=-0.ico)"
	@convert $(<:.tex=-0.ico) -background transparent -gravity center -extent 16x16 $(<:.tex=-0.ico)
	@echo "[MV] $@"
	@mv $(<:.tex=-0.ico) $@

../static/images/logo.png: logo.tex
	@echo "[XELATEX] $<"
	@xelatex -interaction=nonstopmode -shell-escape $< &> /dev/null
	@echo "[MV] $@"
	@mv $(<:.tex=-0.png) $@

.PHONY: clean
clean:
	@rm -f *.aux *.log *.pdf
