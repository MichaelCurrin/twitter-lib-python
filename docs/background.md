# Background

I got tired of duplicating the same common Tweepy logic in each of my projects and having to check how it works each time.

So this project uses cumulative learning to build functionality which gets better in one place and gets reused everywhere by projects which use this project.

Tweepy is a _light_ wrapper on the Twitter API and so it leaves some logic like parameters and response data to be handled by Twitter API or the end user. It also takes a lot of reading of the Twitter API and Tweepy and sample scripts on StackOverflow to figure how to do something which should be straightforward. So this project makes some choices for you, or parametrizes and validates in a way that Tweepy doesn't, so you can use this an easy wrapper on Tweepy to achieve common tasks.

The limitation is that the Twitter API may change and therefore the rules implemented here are no longer valid (e.g. the name or value of a parameter, or the format of returned data). And only a subset of Tweepy functionality is covered and in the preferred approach taken by me. However, this project is still useful both directly and for use in other projects.
