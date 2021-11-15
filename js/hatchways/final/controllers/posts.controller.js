"use strict";

var express = require("express");
var router = express.Router();
var url = require("url");
var jsonParser = express.json();
var Posts = require("../models/posts.model");

router.get("/", jsonParser, (req, res, next) => {
  const model = new Posts();
  const tags = url.parse(req.url, true).query.tags;
  model.readByTags(tags);
  const posts = model.getPosts();
  if (!posts) {
    res.status = 404;
  } else {
    res.status = 200;
    res.json(posts);
  }
});

module.exports = router;
