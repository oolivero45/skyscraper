var out = {};
var elems = document.getElementsByClassName("channel-cell__logo");
for (var i = 0; i < elems.length; i++) {
  var url = elems[i].src.replace("/80/35/", "/640/280/");
  var name = elems[i].alt;
  out[url] = name;
}
var outtext = JSON.stringify(out);
console.log(outtext);
