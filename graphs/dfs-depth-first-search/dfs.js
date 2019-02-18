module.exports = class Graph {

  constructor() {
    this.vertices = {};
    this.edges = {};
    this.visited = [];    
  }
  /*---------------------------------------------------------------------------*/
  addVertex(key){
    this.vertices[key] = key;
    console.log("Added vertex " + key);
  }
  /*---------------------------------------------------------------------------*/
  addEdge(fromKey, toKey, isDirected = false){

    this.edges[fromKey] = toKey;
    
    if(isDirected){
      console.log ("Added edge " + fromKey +" ---> " + toKey);
    } else {
      this.edges[toKey] = fromKey;
      console.log ("Added edge " + fromKey +" <--> " + toKey);
    }
  }
  /*---------------------------------------------------------------------------*/
  visit(vertex) {

    console.log("Hi! I'm at " + vertex);
    this.visited[vertex] = true;

    if (vertex in this.edges) {
      for (let eIdx in this.edges[vertex]) {
        let next = this.edges[vertex][eIdx];
        if (!(next in this.visited)) {
          console.log("I'm going to " + next + " next.")
          this.visit(next);
        } // end if
      } // next e
    } // end if
  } // end visit
  /*---------------------------------------------------------------------------*/
  dfs() {

    this.visited = [];

    for (let i in this.vertices) {
      if (!(i in this.visited)) {
        this.visit(this.vertices[i]);
      } // endif
    } // next i

  } // end DFS  

} // endclass