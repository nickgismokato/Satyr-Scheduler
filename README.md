# SaTyR Scheduler
This is a `Python` package for the production of '*revyer*' within the [SaTyR foundation](https://www.satyr.dk/).

This package will be able to load data files (`.csv`) which contain a list of songs or sketches which will need to be practices and from there create a recommended schedule which will include the title of the sketch/song, which people is involved, if there is need for an instructor, what time the practice will commend and what room the practice will happen in.

Furthermore the program will also take people not doing anything and put them in '**Rekvisitten**'. My goal is also to automatically add breaks within the schedule such that people doesn't have to practice all the time.

### Feature list
- [x] PyPi Package for easy install
- [ ] Full documentation of the package and its uses
- [ ] Automatic scheduler with custom timing, breakpoints, room assignment and instructor assignment

## How to build locally
**NOTE!** To build locally it is recommended to be on a Linux Distro or at least use WSL in windows.

To build locally go into `SatyrScheduler` and run the following command:
```bash
python3 -m build
python3 -m pip install .
```

Remember to also uninstall the package from pip before trying to install. This can be done with the following command:
```bash
pip uninstall SatyrScheduler
```

The script [`clean.sh`](clean.sh) is used to clean the python3 build content. The script [`build.sh`](build.sh) can be used to build the package from scratch without having to clean it.

## How to install
Make sure that `pip` is installed. 

**Install:** To install `SatyrScheduler` run the following command:
```bash
pip install SatyrScheduler
```

**Update:** To update `SatyrScheduler` run the following command:
```bash
pip install --upgrade SatyrScheduler
```


## About SaTyR
