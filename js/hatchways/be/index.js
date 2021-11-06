"use strict";

var express = require("express");
var bodyParser = require("body-parser");
var app = express();
const fs = require("fs");
const path = require("path");

var jsonParser = express.json();

function getRecipes() {
  let rawData = fs.readFileSync(path.resolve(__dirname, "data.json"));
  let parsedData = JSON.parse(rawData);
  return parsedData.recipes;
}

function getRecipe(recipeName) {
  const recipes = getRecipes();
  const recipe = recipes.filter((recipe) => {
    return recipe.name === recipeName;
  });
  if (recipe[0]) {
    return recipe[0];
  } else {
    return undefined;
  }
}

app.get("/recipes", (req, res, next) => {
  const recipes = getRecipes();
  let recipeNames = [];
  for (const recipe of recipes) {
    if (recipe.name) {
      recipeNames.push(recipe.name);
    }
  }
  res.status = 200;
  res.json({ recipeNames });
});

app.post("/recipes", jsonParser, (req, res, next) => {
  const recipeExists = getRecipe(req.body.name);
  if (recipeExists) {
    res.status = 400;
    res.json({ error: "Recipe already exists" });
  } else {
    res.status = 501;
    res.json({ error: "Functionality not implemented yet" });
  }
});

app.get("/recipes/details/:recipeName", (req, res, next) => {
  const recipeName = req.params.recipeName;
  const recipe = getRecipe(recipeName);
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

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
