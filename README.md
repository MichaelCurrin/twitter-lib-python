# Python Twitter Lib
> A wrapper library around Tweepy to make interacting with the Twitter API lighter

[![Python package](https://github.com/MichaelCurrin/python-twitter-lib/workflows/Python%20package/badge.svg)](https://github.com/MichaelCurrin/python-twitter-lib/actions?query=workflow:"Python+package")
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-twitter-lib.svg)](https://GitHub.com/MichaelCurrin/python-twitter-lib/tags/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](#license)

[![Made with Python](https://img.shields.io/badge/Python->%3D3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - tweepy](https://img.shields.io/badge/dependency-tweepy-blue?logo=vue.js&logoColor=white)](https://pypi.org/project/tweepy)

For more info on basic and advanced functionality of Tweepy as well as Twitter policies and docs links, see my [Python Twitter Guide](https://michaelcurrin.github.io/python-twitter-guide/) site.

**Note: This project is still in development and not properly tested.** But, the code here is of good quality and based on experience with Tweepy, so you are welcome to use something you like.


## Features

- Install and use this project in your project, so you can don't have to write low-level Tweepy code yourself. Currently only available as a cloned repo and not as an installable package.
- Save yourself time looking at the Tweepy repo, Tweepy docs and Twitter API docs - use this abstraction layer.
- The logic is centralized and easy to reuse across multiple projects.
- Tweepy parameters are codified as enums - so you get an error if you fail to choose one. See the [constants](twitterlib/constants.py) module.
- Some scripts may run as standalone CLI utilities, so you can perform actions without writing code yourself.


## Documentation

[![View - Online docs](https://img.shields.io/badge/View-Online_docs-2ea44f?style=for-the-badge)](https://michaelcurrin.github.io/python-twitter-lib/)


## Background

I got tired of duplicating the same common Tweepy logic in each of my projects and having to check how it works each time.

So this project uses cumulative learning to build functionality which gets better in one place and gets reused everywhere by projects which use this project.

Tweepy is a _light_ wrapper on the Twitter API and so it leaves some logic like parameters and response data to be handled by Twitter API or the end user. It also takes a lot of reading of the Twitter API and Tweepy and sample scripts on StackOverflow to figure how to do something which should be straightforward. So this project makes some choices for you, or parametrizes and validates in a way that Tweepy doesn't, so you can use this an easy wrapper on Tweepy to achieve common tasks.

The limitation is that the Twitter API may change and therefore the rules implemented here are no longer valid (e.g. the name or value of a parameter, or the format of returned data). And only a subset of Tweepy functionality is covered and in the preferred approach taken by me. However, this project is still useful both directly and for use in other projects.


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
