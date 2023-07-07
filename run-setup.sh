pip install --upgrade pip
pip install --use-pep517 -r requirements.txt

rm -r -f build
rm -r -f dist

python setup.py bdist_wheel
check-wheel-contents dist

echo "\nBuild Success!!!"
