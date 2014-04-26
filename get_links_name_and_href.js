(function() {
    var links = document.querySelectorAll("a");
    
    for(var i=0; i < links.length; i++)
        console.log(links[i].text+";"+links[i].href);
})();
