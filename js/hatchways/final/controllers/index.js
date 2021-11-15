"use strict";

var express = require("express");
var router = express.Router();

router.use("/api/posts", require("./posts.controller"));

module.exports = router;
