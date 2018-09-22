virtualenv -p python3 venv
. venv/bin/activate

git clone git@github.com:Delaware2018/team-8.git
cd team-8
pip3 install requirements.txt

flask run
