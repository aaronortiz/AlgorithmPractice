"use strict";

const { json } = require("express");
var Recipes = require("../models/recipes.model");

var express = require("express"),
  router = express.Router();

var jsonParser = express.json();

router.get("/", (req, res, next) => {
  const recipeNames = Recipes.getRecipeNames();
  res.status = 200;
  res.json({ recipeNames });
});

router.post("/", jsonParser, (req, res, next) => {
  const recipeExists = Recipes.getRecipe(req.body.name);
  if (recipeExists) {
    res.status = 400;
    res.json({ error: "Recipe already exists" });
  } else if (!Recipes.validateRecipe(req.body)) {
    res.status = 400;
    res.json({ error: "Recipe invalid or incomplete" });
  } else {
    Recipes.addRecipe(req.body);
    res.status = 200;
    res.json({});
  }
});

router.put("/", jsonParser, (req, res, next) => {
  const recipeExists = Recipes.getRecipe(req.body.name);
  if (!recipeExists) {
    res.status = 404;
    res.json({ error: "Recipe does not exist" });
  } else {
    Recipes.updateRecipe(req.body);
    res.status = 204;
    res.json({});
  }
});

router.get("/details/:recipeName", (req, res, next) => {
  const recipeName = req.params.recipeName;
  const recipe = Recipes.getRecipe(recipeName);
  res.status = 200;
  if (
    recipe &&
    recipe.ingredients &&
    recipe.instructions &&
    recipe.instructions.length
  ) {
    res.json({
      details: {
        ingredients: recipe.ingredients,
        numSteps: recipe.instructions.length,
      },
    });
  } else {
    res.json({});
  }
});

module.exports = router;
