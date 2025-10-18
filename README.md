# pycharmprojects (aka: my brain on python, splattered)

hi. welcome to my small museum of half-baked ideas, hackerrank-ish attempts, and random experiments i did when i should’ve been sleeping. not too serious, just vibes. warning: typos & chaos are features, not bugs.

- purpose: keep track of my local python doodles from free time.
- language: python (100% lol, till i accidentally add a .txt)
- mood: "it runs on my machine"

## what’s in the box (some of it, anyway)

note: this list is based on what i could see right now, might miss a file or two because, well, attention span. if you wanna snoop the whole set, try the code search here: [GitHub code search](https://github.com/search?q=repo%3Abhardwaj-kushagra%2FPycharmProjects+extension%3Apy&type=code)

- hr stuff (runner-up score-ish):
  - [propy1/hr.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/hr.py)
    - reads a list, yeets the max, then finds 2nd max. classic “find runner up” vibe. prints along the way like a champ.

- strings n things:
  - [propy1/main.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/main.py)
    - `count_substring(string, sub)` counts how many times sub shows up. also has a commented “mutate_string” graveyard. don’t delete (future me, i see you).

- computer vision (aka: i taught my webcam to judge me):
  - [propy1/object.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/object.py)
    - face detection with OpenCV, gender net with Caffe, LBPH recognizer, training data cleanup, background thread, timers… whole circus. needs `haarcascade`, `deploy_gender.prototxt`, `gender_net.caffemodel`, etc. if it errors, u didn’t feed it files. or it’s just moody.

- minimax sum (the one everyone writes once):
  - [propy1/minimaxsumPS-HR.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/minimaxsumPS-HR.py)
    - adds numbers, prints min-sum and max-sum. math but friendly.

- css hex color scavenger:
  - [propy1/hex color code.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/hex%20color%20code.py)
    - scans CSS-y text and prints `#rgb` / `#rrggbb`. comments are spicy, test cases were dramatic. it works, probably.

- triangles but i fell asleep:
  - [propy1/maximunPerimeterTriangle.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/maximunPerimeterTriangle.py)
    - intended to pick a valid triangle with max perimeter. currently… uh… “work in regress”. don’t @ me.

- nested lists (2nd lowest grade club):
  - [propy1/nested lists HR.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/nested%20lists%20HR.py)
    - finds students with second-lowest score and prints names alphabetically. tiny but cute.

- rangoli artist attempt:
  - [propy1/rangoli.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/rangoli.py)
    - was gonna print alphabet rangoli. currently prints… determination. and maybe errors.

- averages (2 decimals or bust):
  - [propy1/finding the percentage.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/finding%20the%20percentage.py)
    - look up a student, average their marks, format to `xx.xx`. precise like a barista.

- email vibes checker:
  - [propy1/validating named email.py](https://github.com/bhardwaj-kushagra/PycharmProjects/blob/a2b49653ee7f2f073138cf9a899992774e80a043/propy1/validating%20named%20email.py)
    - parses "Name <email@host.ext>", validates chars and extension length (<4), prints only the good ones. no fake emails in this house.

## how 2 run (scientific method)
- install python (yep)
- go into the folder n do:
  - `python file_name.py`
- for opencv things you’ll need: `opencv-python`, `numpy`, and the right model files dumped next to the script. if it explodes, that’s part of the charm. read the errors like tea leaves.

## notes to self (and random passerbys)
- this repo is like a junk drawer but i love it anyway.
- if something looks wrong… it might be on porpuse (or not).
- PRs? maybe later. coffee first, fixes later.

ok bye, have a nice code.
