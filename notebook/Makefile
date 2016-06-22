all: 
	cd $(PYLAYERSDOC)/notebook/1-GIS && make rst  
	cd $(PYLAYERSDOC)/notebook/2-AP && make rst  
	cd $(PYLAYERSDOC)/notebook/3-PHY && make rst 
	cd $(PYLAYERSDOC)/notebook/4-MOB && make rst  
	cd $(PYLAYERSDOC)/notebook/5-SIM && make rst 
	cd $(PYLAYERSDOC)/notebook/7-APP && make rst
	cd $(PYLAYERSDOC)/notebook/8-MISC && make rst  
	cd $(PYLAYERSDOC)/notebook/9-PRES && make rst
	cd $(PYLAYERSDOC)/notebook/A-MES && make rst

conv:
	for i in `find . -name "*.ipynb"`;\
	do \
		a=`basename $$i`;\
		b=`dirname $$i`;\
		ipymd --from notebook --to markdown --overwrite $$b/$$a;\
	done	

