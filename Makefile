NAME = IBus-Theme
PACK = IBus Theme Tools
PYPACK = ibus_theme_tools
VERSION = 4.1.3
MSGPOS = $(wildcard $(PYPACK)/locale/*/LC_MESSAGES/*.po)

# for translators: `make mergepo` or `make LANG=YOUR_LANG mergepo`
# The command line passed variable LANG is used to localize pot file.
#
LANGUAGE = $(shell echo $(LANG) | sed -e 's/\..*//')
MSGPOT = locale/$(NAME).pot
MSGDIR = locale/$(LANGUAGE)/LC_MESSAGES
MSGSRC = $(MSGDIR)/$(NAME).po
MSGAIM = $(MSGDIR)/$(NAME).mo

all: _build

clean:
	-rm -fR $(MSGPOS:.po=.po~)
	-rm -fR dist
	-rm -fR build
	-rm -fR deb_dist
	-rm -fR *.tar.gz
	-rm -fR *.pkg.tar.zst
	-rm -fR *.pkg
	-rm -fR pkg src
	-rm -fR bsd/usr
	-rm -fR bsd/plist
	-rm -fR $(PYPACK).egg-info

%.mo: %.po
	msgfmt $< -o $@

build: $(MSGPOS:.po=.mo)

install:
	python3 setup.py install

$(PYPACK)/$(MSGSRC):
	mkdir -p $(MSGDIR); \
	msginit --no-translator --locale $(LANGUAGE).UTF-8 -i ./$(MSGPOT) -o ./$(MSGSRC)

potfile:
	cd $(PYPACK); \
		xgettext -k --keyword=_ --from-code=utf-8 --package-name="$(PACK)" --package-version=$(VERSION) --add-comments='Translators:' --output ./$(MSGPOT) *.py

pofile: $(PYPACK)/$(MSGSRC)

mergepo: potfile pofile
	cd $(PYPACK); \
		msgmerge -U $(MSGSRC) $(MSGPOT); \
		rm -fR $(MSGDIR)/*mo; \
		rm -fR $(MSGDIR)/*po~

rpm:
	python3 setup.py bdist_rpm

deb:
	python3 setup.py --command-packages=stdeb.command sdist_dsc --default-distribution hirsute --copyright-file LICENSE bdist_deb

ppa: deb
	cd deb_dist; \
		debsign *source.changes; \
		dput ibus-theme-tools *source.changes

bsdbuild:
	python setup.py install --root="`pwd`/bsd" --optimize=1
	cd bsd; \
		for dir in `find usr -type f`; do \
			echo $$dir >> plist; \
		done

bsd: bsdbuild
	cd bsd; \
		pkg create -m . -r . -p plist -o ..

arch:
	makepkg --printsrcinfo > .SRCINFO
	makepkg

upload:
	python3 -m build
	python3 -m twine check dist/*
	python3 -m twine upload dist/*
