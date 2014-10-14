---
layout: post
title: Week 4 Extra Credit
week: 4
permalink: week-4-extra/
---

See individual pages for resource links.

* [Requests Quickstart/Tutorial](http://docs.python-requests.org/en/latest/user/quickstart/)

### Weather APIs

* Can you write a function that answers the question: "Do I need an umbrella tomorrow morning?"

### Other APIs

* Using the [GitHub API](https://developer.github.com/v3/repos/#list-user-repositories):
  * print out a user's repositories given their username
  * print a summary of the unique languages used in their repositories
  * print a summary of the percentage of each language they used
  * figure out which language is most used and print out a sentence saying '_username_ is an awesome _language_name_ developer!'
  * use a list of adjectives to make that sentence more random and interesting
   
* Using the Twitter API:
  * set up a new account that people can @-mention with a phrase, like
    _@hackeroracle what's my score? github jennielees_
  * use the Twitter API to check @-mentions on this account and try to pull out the GitHub username from it - you can assume a fairly strict adherence to the above format
  * once you have the username, use the GitHub functions you wrote above to create a reply tweet to the original user, with a nice sentence about how great a developer they are!
  * think about issues with this: how do you make sure you don't send the same tweet twice?
    