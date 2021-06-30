NAME = IBus-Theme
PACK = IBus Theme Tools
VERSION = 1
MSGPOS = $(wildcard locale/*/LC_MESSAGES/*.po)

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
	-rm -fR $(MSGPOS:.po=.mo)
	-rm -fR $(MSGPOS:.po=.po~)

%.mo: %.po
	msgfmt $< -o $@

install: $(MSGPOS:.po=.mo)

$(MSGSRC):
	mkdir -p $(MSGDIR); \
	msginit --no-translator --locale $(LANGUAGE).UTF-8 -i ./$(MSGPOT) -o ./$(MSGSRC)

potfile:
	xgettext -k --keyword=_ --from-code=utf-8 --package-name="$(PACK)" --package-version=$(VERSION) --add-comments='Translators:' --output ./$(MSGPOT) *.py

pofile: $(MSGSRC)

mergepo: potfile pofile
	msgmerge -U $(MSGSRC) $(MSGPOT); \
	rm -fR $(MSGPOT); \
	rm -fR $(MSGDIR)/*po~
