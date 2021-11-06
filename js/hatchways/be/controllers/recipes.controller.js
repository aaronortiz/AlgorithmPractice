"use strict";

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
  } else {
    res.status = 200;
    res.json({ error: "Functionality not implemented yet" });
  }
});

router.get("/details/:recipeName", (req, res, next) => {
  const recipeName = req.params.recipeName;
  const recipe = Recipes.getRecipe(recipeName);
  res.status = 200;
  if (recipe && recipe.ingredients) {
    res.json({
      details: {
        ingredients: recipe.ingredients,
        numSteps: recipe.ingredients.length,
      },
    });
  } else {
    res.json({});
  }
});

module.exports = router;
