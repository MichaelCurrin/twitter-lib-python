# Features

- This is a high-level CLI.
    - It handles common Twitter API tasks.
    - It makes some choices for you on approach and takes care of implementation details like, so you can focus on writing your logic.
    - You can don't have to write low-level Tweepy code yourself or read the Tweepy docs.
    - Save yourself time looking at the Tweepy repo, Tweepy docs and Twitter API docs - use this abstraction layer.
- Install and use this project. Currently only available as a cloned repo and not as an installable package.
- The logic is centralized and easy to reuse across multiple Twitter projects. This saves having to copy and maintain long Tweepy boilerplate code all over.
- Rules from the Twitter API are enforced here, making up for Tweepy's like of handling those.
     - Tweepy parameters are codified as enums - so you get an error if you fail to choose a valid value. See the `twitterlib/constants.py` module.
- Some scripts may run as standalone CLI utilities, so you can perform actions without writing code yourself.
