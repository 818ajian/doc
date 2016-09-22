SRC= $(wildcard *.md)
IPYNB= $(SRC:.md=.ipynb)
RST= $(SRC:.md=.rst)

ipynb: $(IPYNB) 

rst: $(RST)

%.ipynb: %.md
	notedown $< --to notebook > $@

%.rst: %.ipynb
	echo "====================" >> ../errors.log
	echo $< >> ../errors.log
	echo "====================" >> ../errors.log
	jupyter nbconvert $< --to rst --execute
	utf82ascii $@
