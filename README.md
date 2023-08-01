# ContestScheduler

Instructions for local:

1. checkout this branch using `git checkout caleb-dev`
2. create a new virtualenv using python with the command `python3 -m venv projectenv`
3. activate the venv using `source projectenv/bin/activate`
4. install dependencies using `pip install -r requirements.txt`
5. run `flask run` to start the flask application hosted at `http://127.0.0.1:5000`

Instructions through docker:
1. Install the docker desktop application
2. Navigate to the ContestScheduler folder and check out this branch using `git checkout caleb-dev`
3. Build the docker container using `docker build -t scheduler .`
4. Run the docker container using `docker run -p 8000:8000 --shm-size=2g scheduler`
