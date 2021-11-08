"use strict";

const fs = require("fs");
const path = require("path");

class Recipes {
  static read() {
    let rawData = fs.readFileSync(path.resolve(__dirname, "data.json"));
    let parsedData = JSON.parse(rawData);
    return parsedData.recipes;
  }

  static write(recipes) {
    const rawData = JSON.stringify({ recipes });
    const fname = `${__dirname}/data.json`;
    fs.writeFile(fname, rawData, "utf8", () => {
      console.log("Success");
    });
  }

  static updateRecipe(recipe) {
    if (Recipes.validateRecipe(recipe)) {
      const recipes = this.read();
      for (let i = 0; i < recipes.length; i++) {
        if (recipes[i] && recipes[i].name && recipes[i].name === recipe.name) {
          recipes[i] = recipe;
          Recipes.write(recipes);
          return;
        }
      }
    }
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

  static validateRecipe(recipe) {
    return (
      recipe.name &&
      recipe.ingredients &&
      recipe.ingredients.length &&
      recipe.ingredients.length > 0 &&
      recipe.instructions &&
      recipe.instructions.length &&
      recipe.instructions.length > 0
    );
  }

  static addRecipe(recipe) {
    if (Recipes.validateRecipe) {
      let recipes = Recipes.read();
      recipes.push(recipe);
      Recipes.write(recipes);
    } else {
      console.error("Recipe is invalid or incomplete");
    }
  }
}

module.exports = Recipes;
