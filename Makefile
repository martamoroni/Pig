PYTHON ?= python


version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHONE)
	$(PYTHON) --version



venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	$printf ". .venv/Scripts/sctivate\n"


install:
	$(PYTHON) -m pip install -r requirements.txt


installed:
	$(PYTHON) -m pip list


clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


pylint:
	@$(call MESSAGE,$@)
	-cd guess && $(PYTHON) -m pylint *.py


flake8:
	
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint



black:
	
	@$(call MESSAGE,$@)
	$(PYTHON) -b black Pig/ test/


codestyle: black



unittest:
	
	@$(call MESSAGE,$@)
	$(PYTHON) -m unittest discover


coverage:

	@$(call MESSAGE,$@)
	coverage run -m unittest discover
	coverage html
	coverage report -m

test: lint coverage




pydoc:

	@$(call MESSAGE,$@)
	install -d doc/pydoc
	$(PYTHON) -m pydoc -w Pig/*.py
	mv *.html doc/pydoc


pdoc:
	
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/pdoc Pig/*.py


pyreverse:

	@$(call MESSAGE,$@)
	install -d doc/pyreverse
	pyreverse guess/*.py
	dot -tpng classes.dot -o doc/pyreverse/classes.png
	dot -tpng packages.dot -o doc/pyreverse/packages.png
	rm -f classes.dot packages.dot

doc: pdoc pyreverse #pydoc sphinx


radon-cc:

	@$(call MESSAGE,$@)
	radon cc -show-complexity --average Pig

radon-mi:

	@$(call MESSAGE,$@)
	radon mi --show Pig

radon-raw:

	@$(call MESSAGE,$@)
	radon raw Pig

radon-hal:

	@$(call MESSAGE,$@)
	radon hal Pig

cohesion:

	@$(call MESSAGE,$@)
	cohesion --directory Pig

metrics: radon-cc radon-mi radon-raw radon-hal cohesion


bandit:

	@$(call MESSAGE,$@)
	bandit --recursive Pig

