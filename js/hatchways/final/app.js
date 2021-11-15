"use strict";

var express = require("express");
var app = express();

app.use(require("./controllers"));

app.listen(3000, () => {
  console.log("Blog post API running on port 4321");
});
