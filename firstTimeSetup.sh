set -e

source environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate

pip install pip wheel autopep8 --upgrade
pip install -r requirements.txt
