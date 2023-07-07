rm -r -f build
rm -r -f dist

python setup.py bdist_wheel
check-wheel-contents dist

echo "\n Build Success!!!"

pip install dist/databricks_sdk_demo-1.0-py3-none-any.whl --force-reinstall