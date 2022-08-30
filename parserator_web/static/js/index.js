/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */


export default class App {

   constructor(routeUrl){
      this.routeUrl = routeUrl
      document.addEventListener('DOMContentLoaded', this.start.bind(this))
   }


   start(){
      const inputAddress = document.getElementById('address')
      document.getElementById("submit").addEventListener("click", this.start)
   }
} 
