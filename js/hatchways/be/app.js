"use strict";

var express = require("express");
var app = express();

app.use(require("./controllers"));

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
