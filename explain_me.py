"""
Explain me!
This script would give you a list of commonly used commands, its source, and explain what these commands do in simple English.
"""

common_commands_list = [
    {
        "type":"explain-me",
        "question":"pip install --upgrade robotframework-seleniumlibrary",
        "src":"https://github.com/robotframework/SeleniumLibrary",
        "answers":['Install Python-specific modules and use --upgrade to upgrade the existing python specific module']
    },
    {
        "type":"explain-me",
        "question":"sudo pip install -r requirements.txt",
        "src":"https://github.com/qxf2/qxf2-page-object-model",
        "answers":['Install pre-requisite libraries/dependencies']
    },
    {
        "type":"explain-me",
        "question":"git submodule sync",
        "src":"https://git-scm.com/book/en/v2/Git-Tools-Submodules",
        "answers":["Apply the remote repo's configuration to your local submodule repos. Make the child repo follow the parent repo. It is similar to master/slave"]
    },
    {
        "type":"explain-me",
        "question":"source path to python exe location/scripts/activate",
        "src":"https://gist.github.com/simonw/4835a22c79a8d3c29dd155c716b19e16",
        "answers":['Activating python virtualenv']
    },
    {
        "type":"explain-me",
        "question":"sudo apt-get update && sudo apt-get upgrade && sudo apt-get install",
        "src":"https://github.com/M4cs/BabySploit",
        "answers":['These are the common commands in Linux to install and upgrade packages.']
    },
    {
        "type":"explain-me",
        "question":"python -m http.server {port}",
        "src":"https://github.com/IBM/ibm.github.io",
        "answers":['To run the tests on the desired port or to test changes locally.']
    },
    {
        "type":"explain-me",
        "question":"docker-compose up --build",
        "src":"https://github.com/PokeAPI/pokeapi",
        "answers":['To start the process in detached mode and specify the -d switch to start in detached mode.']
    },
    {
        "type":"explain-me",
        "question":"curl -L https://git.io/rustlings | bash",
        "src":"https://github.com/rust-lang/rustlings",
        "answers":['To install the package to the default path']
    },
    {
        "type":"explain-me",
        "question":'xvfb-run --server-args="-screen 0 1024x768x24" python test_script.py',
        "src":"https://github.com/joyzoursky/docker-python-chromedriver",
        "answers":['To run the script in a headless display screen with the given dimensions.']
    },
    {
        "type":"explain-me",
        "question":"ssh -i /Users/yaroslav/.ncluster/ncluster5-yaroslav-316880547378-us-east-1.pem -o StrictHostKeyChecking=no ubuntu@18.206.193.26tmux a",
        "src":"https://github.com/joyzoursky/docker-python-chromedriver",
        "answers":['Ssh/Login into a Ubuntu instance using a .pem file(trust chain with user identification) where host key is not being checked for login purposes.']
    }
]

# Start of the script
if __name__ == "__main__": 
    print ("Here is the list of common commands that we use: %s" %common_commands_list) 