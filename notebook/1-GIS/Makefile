SRC= $(wildcard *.md)
IPYNB= $(SRC:.md=.ipynb)
RST= $(SRC:.md=.rst)

clean:
	rm *.ipynb

ipynb: $(IPYNB) 

rst: $(RST)

%.ipynb: %.md
	notedown $< --to notebook > $@

%.rst: %.ipynb
	echo "====================" >> ../errors.log
	echo $< >> ../errors.log
	echo "====================" >> ../errors.log
	runipy -o --skip-exception $<  >/dev/null 2>> ../errors.log
	jupyter nbconvert $< --to rst 
	utf82ascii $@
