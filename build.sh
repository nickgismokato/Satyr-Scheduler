#Uninstall SatyrScheduler
pip uninstall SatyrScheduler -y

#Removes the folders and files created by the python3 build process
rm -rf SatyrScheduler/dist
rm -rf SatyrScheduler/build
rm -rf SatyrScheduler/src/SatyrScheduler.egg-info

#Building the application
cd SatyrScheduler && python3 -m build

#Local Install
python3 -m pip install .