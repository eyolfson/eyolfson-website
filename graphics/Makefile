all: ../static/images/favicon.png ../static/images/icon.png

../static/images/%.png: %.tex
	@echo "[XELATEX] $<"
	@xelatex -interaction=nonstopmode -shell-escape $< &> /dev/null
	@echo "[CONVERT] $(<:.tex=-0.png)"
	@convert $(<:.tex=-0.png) -background transparent -gravity center -extent 32x32 $(<:.tex=-0.png)
	@echo "[MV] $@"
	@mv $(<:.tex=-0.png) $@

.PHONY: clean
clean:
	@rm -f *.aux *.log *.pdf
