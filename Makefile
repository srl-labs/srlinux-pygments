MKDOCS = ghcr.io/squidfunk/mkdocs-material:9.0.2
# insiders version/tag https://github.com/srl-labs/mkdocs-material-insiders/pkgs/container/mkdocs-material-insiders
MKDOCS_INS = ghcr.io/srl-labs/mkdocs-material-insiders:8.5.11-insiders-4.27.0-hellt

# run this target and then call `mkdocs serve -a 0.0.0.0:8000` to run a webserver
# re-run the web server when changes are made to the lexer.
.PHONY: test
test:
	docker run -it --rm -p 8010:8000 \
		-v $(CURDIR)/test:/docs \
		-v $(CURDIR):/srlinux-pygments \
		--entrypoint '' \
		$(MKDOCS) \
		ash -c 'pip install -e /srlinux-pygments && ash'