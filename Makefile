.PHONY: testdirs

OUT_DIR = testcase/cascade_test/feature_path\
	testcase/test_cases_rule/feature_path

tests: ${OUT_DIR}
	nosetests -v --exe

${OUT_DIR}:
	mkdir -p ${OUT_DIR}
