# FelPy

## Intro

This is an assortment of Python tools that I have/will write/n, usually because they help me. If something that I've bodged
together can be made to work within 4h of work to a standard I can publish, I'll throw it in here

## Install

These tools are all published as one package, but are all used with seperate import statements. To install:

```bash

sudo pip install FelPy

```

This will install everything automagically.

## Usage

### listFormat

This uses the import `listFormat`.
It uses a class, and must be instantiated as follows:

```python

variableName = listFormat.Formatter()

```

If you wish to give it an list to start, just put one inbetween the brackets. The list can be added to like so:
```python
variableName.add("List item")
```
To randomize, or scramble, the order of the items in the list, run:
```python
variableName.randomize()
```
To simply take out the raw list, run:
```python
variableName.simpleOutput()
```

Or, to format to a 2D list, use:
```python
variableName.formatOutput(x,y)
```
Where x and y are the width and height of the desired list.

All of the above methods work standalone.

```python
print(listFormat.random(["a","b"]))

print(listFormat.formatOutput(["a","b","c","d"],2,2))

```


### confReturn
This is another import, `confReturn`

Very simply, run it like so:

```python
variableName = confReturn.do("gender")
```
Where `"gender"` can be any string being set. Play arround with it in IDLE, you'll get the gist of it.

###leaderboard
For this one, import `leaderboard`

It will generate a 10 line leaderboard. You can write to it with a name, up to 10
characters, and a points value, between 0 and 99. When placing entries, they are sorted first
by value, so higher scores occur higher up. If you are adding an entry when there is already
an entry with the same points value, the new entry will appear above.

All of the functions below will accept one (more) parameter, the filename. Without it, it
will default to `filename.txt`. Leaderboard data is stored as UTF-8 text, but can be given
any file extension. NB: Remember to include a file extension (I personally like `.lbd`) if
you are using a custom filename.

To generate (or clear) a leaderboard:
```python
leaderboard.make()
```

To write to the leaderboard:
```python
leaderboard.write(points, name)
```

To read the leaderboard (outputs as a 10-line String):
```python
leaderboard.read()
```

## Contributions

Financial aid is always welcome at [Paypal](https://www.paypal.me/felixj20000), or of couse feel free to fork the project. If you
do fork, please make pull requests back - I am always looking to improve my work.
