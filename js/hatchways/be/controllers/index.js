"use strict";

var express = require("express"),
  router = express.Router();

router.use("/recipes", require("./recipes.controller"));

module.exports = router;
