  function searchFunction() {
    input = document.getElementById('searchInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("item_list");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
      p = li[i].getElementsByTagName("a")[0];
      txtValue = p.textContent;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        li[i].style.display = "";
      } else {
        li[i].style.display = "none";
      }
    }
  }

	$.getJSON( "items.json", function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push("<li class=\"list-group-item\"><a id=\"itemname\">" + key.toUpperCase() + "</a> <a id=\"itemprice\">"+ val + " ₽</a></li>");
    document.getElementById("item_list").innerHTML = items.join('');
  });
  $({
  }).appendTo( "body" );
  });

 function fetchHeader(url, wch) {
    try {
        var req=new XMLHttpRequest();
        req.open("HEAD", url, false);
        req.send(null);
        if(req.status== 200){
            return req.getResponseHeader(wch);
        }
        else return false;
    } catch(er) {
        return er.message;
    }
}

window.onload = function () {
    var datum = fetchHeader('items.json','Last-Modified');
    document.getElementById("foten").innerHTML = "Last updated " + datum;
}

