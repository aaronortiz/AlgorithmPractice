#! /usr/bin/env node

const readlineSync = require('readline-sync');
const DFSGraph = require('./dfs');
let dontStahp = readlineSync.keyInYN("Let's make a graph, shall we?");

if(!dontStahp) return 0;

const vertexCount = readlineSync.questionInt("\nHow many vertices (nodes) does your graph have?: ");
const edgeCount =  readlineSync.questionInt("How many edges (connections) does your graph have?: ");
const directed = readlineSync.keyInYN("Do the edges in your graph have a single direction (directed vs undirected graph)? ");

const myGraph = new DFSGraph();

console.log('\n');

for(let i = 0; i < vertexCount; i++){
  myGraph.addVertex(readlineSync.question("Enter a vertex: ", { limit: /[A-Za-z]/ }));
}

console.log("\nVertices: ");
console.log(myGraph.vertices);
console.log('\n');

for(let currEdge = 1; currEdge <= edgeCount; currEdge++){

  let from = "";
  let dest = "";

  while (!(from in myGraph.vertices)) {
    from = readlineSync.question("Enter the start vertex for edge " + currEdge + ": ");
    if (!(from in myGraph.vertices)) {
      console.log("Vertex " + from + " is not part of your graph. Try one of these: ");
      console.log(myGraph.vertices);
    }
  }

  while (!(dest in myGraph.vertices)) {
    dest = readlineSync.question("Enter the end vertex for edge " + currEdge + ": ");
    if (!(dest in myGraph.vertices)) {
      console.log("Vertex " + dest + " is not part of your graph. Try one of these: ");
      console.log(myGraph.vertices);
    }
  }
  myGraph.addEdge(from, dest, directed);

}

dontStahp = readlineSync.keyInYN("\nShall we traverse the graph?\n");

if (dontStahp){
  console.log("OK, here we go:\n");
  myGraph.dfs();
}
