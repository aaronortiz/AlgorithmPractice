"use strict";

const fs = require("fs");
const path = require("path");

class Recipes {
  static read() {
    let rawData = fs.readFileSync(path.resolve(__dirname, "data.json"));
    let parsedData = JSON.parse(rawData);
    return parsedData.recipes;
  }

  static getRecipe(recipeName) {
    const recipes = this.read();
    const recipe = recipes.filter((recipe) => {
      return recipe.name === recipeName;
    });
    if (recipe[0]) {
      return recipe[0];
    } else {
      return undefined;
    }
  }

  static getRecipeNames() {
    const recipes = Recipes.read();
    let recipeNames = [];
    for (const recipe of recipes) {
      if (recipe.name) {
        recipeNames.push(recipe.name);
      }
    }
    return recipeNames;
  }
}

module.exports = Recipes;
