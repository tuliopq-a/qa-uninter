#!/bin/bash
echo "==== Running Pytest Functional Tests ===="

pytest tests/functional --disable-warnings --maxfail=1 | tee /qa/pytest.log

echo "==== Pytest Completed ===="
