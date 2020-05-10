# Python Twitter Lib
> A wrapper library around Tweepy to make interacting with the Twitter API lighter

[![Actions status](https://github.com/MichaelCurrin/python-twitter-lib/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/python-twitter-lib/actions)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/python-twitter-lib.svg)](https://GitHub.com/MichaelCurrin/python-twitter-lib/tags/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](#license)



## Features

- Install and use this project in your project, so you can don't have to write low-level Tweepy code yourself.
- Same yourself time looking at the Tweepy repo, Tweepy docs and Twitter API docs - use this abstraction layer.
- The logic is centralized and easy to reuse across multiple projects.
- Some scripts may run as standalone utilities so you can perform actions without writing code yourself.



## Example usage

_TODO: Screenshot or command-line snippet._


## Documentation

_TODO: Either delete this Documentation section and the `docs` folder, or delete the Installation, Usage and Development sections below._

See project [docs](/docs/).


## Installation

_TODO: Put your installation instructions here._


## Usage

_TODO: Put your usage instructions here._


## Development

_TODO: Put your developer instructions here._



## Background

I got tired of duplicating the same common Tweepy logic in each of my projects and having to check how it works each time.

So this project uses cumulative learning to build functionality which gets better in one place and gets reused everywhere by projects which use this project.

Tweepy is a _light_ wrapper on the Twitter API and so it leaves some logic like parameters and response data to be handled by Twitter API or the end user. It also takes a lot of reading of the Twitter API and Tweepy and sample scripts on StackOverflow to figure how to do something which should be straightforward. So this project makes some choices for you, or parametrizes and validates in a way that Tweepy doesn't, so you can use this an easy wrapper on Tweepy to achieve common tasks.

The limitation is that the Twitter API may change and therefore the rules implemented here are no longer valid (e.g. the name or value of a parameter, or the format of returned data). And only a subset of Tweepy functionality is covered and in the preferred approach taken by me. However, this project is still useful both directly and for use in other projects.


## License

Licensed under [MIT](/LICENSE).
