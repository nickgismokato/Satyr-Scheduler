# SaTyR Scheduler
This is a `Python` package for the production of '*revyer*' within the [SaTyR foundation](https://www.satyr.dk/).

This package will be able to load data files (`.csv`) which contain a list of songs or sketches which will need to be practices and from there create a recommended schedule which will include the title of the sketch/song, which people is involved, if there is need for an instructor, what time the practice will commend and what room the practice will happen in.

Furthermore the program will also take people not doing anything and put them in '**Rekvisitten**'. My goal is also to automatically add breaks within the schedule such that people doesn't have to practice all the time.

## How to build locally
To build locally go into `SatyrScheduler` and run the following command:
```bash
python3 -m build
python3 -m pip install .
```

Remember to also uninstall the package from pip before trying to install. This can be done with the following command:
```bash
pip uninstall SatyrScheduler
```

## How to install
Make sure that `pip` is installed. To install `SatyrScheduler` run the following command:
```bash
pip install SatyrScheduler
```