"use strict";

var request = require("request");
const hostname = "https://api.hatchways.io";

class Post {
  author;
  authorId;
  id;
  likes = 0;
  popularity = 0.0;
  reads = 0;
  tags = [];

  constructor(props) {
    if (props && props.author) {
      this.author = props.author;
    }

    if (props && props.authorId) {
      this.authorId = props.authorId;
    }

    if (props && props.id) {
      this.id = props.id;
    }

    if (props && props.likes) {
      this.likes = props.likes;
    }

    if (props && props.popularity) {
      this.popularity = props.popularity;
    }

    if (props && props.tags) {
      this.tags = props.tags;
    }
  }
}

class Posts {
  posts = [];
  cache = [];

  constructor() {
    this.posts = [];
    this.cache = [];
  }

  getPosts() {
    return this.posts;
  }

  readByTag(tag) {
    const url = `${hostname}/assessment/blog/posts?tag=${tag}`;

    request
      .get(url)
      .on("error", (error, response) => {
        if (error) {
          throw new Error(error);
        }
      })
      .on("response", (response) => {
        if (response.body) {
          const body = JSON.parse(response.body);
          if (Array.isArray(body.posts)) {
            for (const post of body.posts) {
              this.addPost(new Post(post), tag);
            }
          }
        }
      });
  }

  readByTags(tags) {
    if (tags) {
      for (const tag of tags) {
        if (!this.cache[tag]) {
          // Keeps a cache of tags read in the past
          this.readByTag(tag);
        }
      }
    }
  }

  addPost(post, tag) {
    if (post) {
      this.posts.push(new Post(post));
      if (!this.cache[tag]) {
        this.cache[tag] = [];
      }
      this.cache[tag].push(post);
    }
  }
}

module.exports = Posts;
